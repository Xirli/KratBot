from telebot import *

from Residents import *
from config import *
from Actions import *

RESIDENTS = read_xml()
bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def regist_button(message):
    user_is_ban(message)
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Получить паспорт", callback_data="regist")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Тебя мне очень не хватает!", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "regist")
def regist_user_call(call):
    if not user_chek_ban("ban", call.from_user):
        regist_user(call.message.chat.id, call.from_user)


def regist_user(chat, user):
    r = new_resident(user, RESIDENTS)
    if r is None:
        bot.send_message(chat, TEXT['regist 0'])
    else:
        bot.send_message(chat, TEXT['regist 1'])
        r.money += 102 - len(RESIDENTS)
        bot.send_message(chat, TEXT['regist 2'])
        bot.send_message(chat, get_stat([r]))
        RESIDENTS.append(r)
        write_xml(RESIDENTS)


@bot.message_handler(commands=['pay'])
def start(message):
    user_is_ban(message)

    if message.reply_to_message is None:
        bot.send_message(message.chat.id, TEXT['pay 1'])
        return
    if len(message.text) < 5:
        bot.send_message(message.chat.id, TEXT['pay 2'])
        return

    try:
        money = int(message.text[5:])
    except ValueError:
        bot.send_message(message.chat.id, TEXT['pay 3'])
        return

    if money < 0:
        bot.send_message(message.chat.id, TEXT['pay 4'])
        return

    sender = get_resident(message.from_user, RESIDENTS)
    receiver = get_resident(message.reply_to_message.from_user, RESIDENTS)

    if sender is None:
        bot.send_message(message.chat.id, TEXT['pay 5'])
        regist_button(message)
        return
    if receiver is None:
        bot.send_message(message.chat.id, TEXT['pay 6'])
        regist_button(message)
        return
    if receiver == sender:
        bot.send_message(message.chat.id, TEXT['pay 7'])
        return
    if sender.money - money < 0:
        bot.send_message(message.chat.id, TEXT['pay 8'])
        return

    sender.money -= money
    receiver.money += money
    write_xml(RESIDENTS)

    bot.send_message(message.chat.id, get_stat([sender, receiver]))


@bot.message_handler(commands=['fire'])
def start(message):
    user_is_ban(message)

    if message.reply_to_message is None:
        bot.send_message(message.chat.id, TEXT['fire 1'])
        return

    attacker = get_resident(message.from_user, RESIDENTS)
    victim = get_resident(message.reply_to_message.from_user, RESIDENTS)

    if attacker is None:
        bot.send_message(message.chat.id, TEXT['fire 2'])
        regist_button(message)
        return
    if victim is None:
        bot.send_message(message.chat.id, TEXT['fire 3'])
        regist_button(message)
        return
    if attacker == victim:
        bot.send_message(message.chat.id, TEXT['fire 4'])
    if attacker.money < 1:
        bot.send_message(message.chat.id, TEXT['fire 5'])
        return

    # write_xml(RESIDENTS)
    attacker.money -= 1
    action = Action("ban", 15)
    victim.list_ban.append(action)
    bot.send_message(message.chat.id, "Время действия: 30 сек")


@bot.message_handler(commands=['stat_all'])
def start(message):
    user_is_ban(message)
    bot.send_message(message.chat.id, get_stat(RESIDENTS))


@bot.message_handler(commands=['stat'])
def start(message):
    if user_chek_ban(message):
        bot.send_message(message.chat.id, get_resident(message.from_user, RESIDENTS).first_name + " is banned")
    bot.send_message(message.chat.id, get_stat([get_resident(message.from_user, RESIDENTS)]))


def get_stat(residents):
    stat = ""
    for res in residents:
        if res is None:
            return TEXT['get_stat']
        stat += res.first_name + ': '
        stat += str(res.money)
        stat += " тёмкоин\n" if (res.money % 10 == 1) else " тёмкоина\n" if (
                1 < (res.money % 10) < 5) else " тёмкоинов\n"
    return stat


@bot.message_handler(content_types=['text'])
def reg(message):
    user_is_ban(message)


def user_is_ban(message):
    if user_chek_ban("ban", message.from_user):
        bot.delete_message(message.chat.id, message.message_id)


def user_chek_ban(action_name, from_user):
    user = get_resident(from_user, RESIDENTS)
    if user is None:
        return False
    for act in user.list_ban:
        if act.name == action_name:
            if act.time_end < time():
                user.list_ban.remove(act)
            else:
                return True
    return False


bot.polling()
