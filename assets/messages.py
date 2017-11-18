from .button import create_button
from . import main

username = {
    'get_name': '🤵 Ну что будем знакомиться? Напиши своё имя пожалуйста',
    'unknown_message': 'Прости но ты втираешь мне какую то дичь!',
    'success_get_name': '''
As for today (23 Nov 2016) we have the following:
1) iOS users can format messages with bold and italic font using official app. They just select text and apply formatting.
2) Android and Desktop users can apply monowidth formatting to their text using single (inline) and triple (block) backticks.
3) Bots can use Markdown or HTML formatting. Some people, including me, are using some services to post formatted text via bots to channels/groups.
4) Plus Messenger (unofficial Telegram client for Android) has a special feature: you format text via any bot, e.g. @bold, and send it to yourself (or whatever you want). Then you forward it to desired chat with disabled quotting (I don't remember exactly how that is named, sorry). As a result, you get formatted-by-@bold message sent as if it was yours, without any "via @bot" markings.
    '''
}

handler_reply_button = [
    {
        'name': 'Быстрый поиск',
        'run': create_button.search_mentor_btn,
        'text': 'Отправьте мне Имя и Фамилию искаемого Вами ментора и нажмите кнопку "Найти"'
    },
    {
        'name': 'Помочь',
        'run': create_button.help_slide_btn,
        'text': '''
Хорошо поставленный вопрос — тот, 
на который участник деловой беседы захочет ответить, 
сможет ответить или над которым ему захочется подумать, 
и он будет заинтересован в сотрудничестве. 
Умение ставить вопросы есть необходимый признак ума или проницательности.
'''        
    },
    {
        'name': 'Найти',
        'run': main.searching_mentor,
        'text': 'Поиск окончен!'
    },
    {
        'name': 'Все менторы',
        'run': main.get_all_mentors,
        'text': 'Поиск окончен!'
    },
    {
        'name': 'Закрыть',
        'run': create_button.start_buttons,
        'text': 'Поиск окончен!'
    },
    {
        'name': 'Назад',
        'run': create_button.help_slide_btn,
        'text': 'Я помогаю тебе!'
    },
    {
        'name': 'Дальше',
        'run': main.searching_mentor,
        'text': 'Поиск окончен!'
    }
]

# (''')о___о(''')
#  \ ' (о_о) / /
#   \ \ _Ш_ / /
#    | . . . |
#    | . . . |
#    /./o|o\.\
#   / /  u  \ \
# („„„)     („„„)
# Я мишка, мишки, мишка,
#    Я менторов ищу!

# Основной язык на котором пишите?
