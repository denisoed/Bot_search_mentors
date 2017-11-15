from .button import create_button
from . import main


username = {
    'get_name': '🤵 Ну что будем знакомиться? Напиши своё имя пожалуйста',
    'unknown_message': 'Прости но ты втираешь мне какую то дичь!',
    'success_get_name': '🤵 Прекрасно!\n\n Я приготовил для тебя тут пару инструкций:\n \
    1) Если ты уже знаешь имя и фамилию того кто тебе нужен жми "Быстрый поиск"\n \
    2) Если же есть какие то трудности у тебя, я могу помочь, жми "Помочь"'
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
        'text': 'Я помогаю тебе!'
    },
    {
        'name': 'Найти',
        'run': main.searching_mentor,
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
