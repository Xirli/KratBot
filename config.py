from secret_file import TOKEN
from secret_file import RES_FILE

# TOKEN - token for telebot
# RES_FILE - name of xml file that contains info of residents

TEXT = {}
TEXT['regist 0'] = "Ты уже являешся жителем Тёмы. Спи спокойно."
TEXT['regist 1'] = "Поздравляю, теперь ты житель Тёмы!"
TEXT['regist 2'] = "Тебе на счёт пришёл подарок, Тёмкоины!"
TEXT['pay 1'] = "Если вы хотите переслать деньги, нужно ответить на сообщегие получателя командой /pay ###\nвместо ### напишите сумму, которую хотите перечислить."
TEXT['pay 2'] = "Если вы хотите переслать деньги, нужно ответить на сообщегие получателя командой /pay ###\nвместо ### напишите сумму, которую хотите перечислить."
TEXT['pay 3'] = "В качестве второго параметра вводите число (количество пересылаемых тёмкоинов)"
TEXT['pay 4'] = "Не, так нельзя)"
TEXT['pay 5'] = "Ты ещё не являешся жителем Тёмы, получи паспорт!"
TEXT['pay 6'] = "Получатель не является жителем Тёмы, попроси его получить паспорт!"
TEXT['pay 7'] = "Нельзя! Вселенная схлопнется!"
TEXT['pay 8'] = "У тебя не достаточно тёмкоинов. Заработай их, а потом трать!"
TEXT['get_stat'] = "Все вымерли..."
TEXT['fire 1'] = 'Ответте на сообщение пользователя, которого вы хотите забанить'
TEXT['fire 2'] = 'Перед тем как атаковать станте жителем Тёмы'
TEXT['fire 3'] = 'Тот, кого вы атакуете не является жителем Тёмы, да, он нехороший!'
TEXT['fire 4'] = 'Вы решили забанитть себя? Ну ладно...'
TEXT['fire 5'] = 'У вас не достаточно тёмкоинов'
