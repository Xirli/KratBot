list_message = []


def send_message(bot, chat_id, text, replymarkup=None):
    if len(list_message) == 2:
        message = list_message.pop(0)
        bot.delete_message(message.chat.id, message.message_id)
        bot.delete_message(message.chat.id, message.message_id - 1)
    list_message.append(bot.send_message(chat_id, text, reply_markup=replymarkup))

"""
    send_message успешно удаляет сообщения,
    если их количество парное (команда юзера и сообщение бота),
    требует исправления
"""
