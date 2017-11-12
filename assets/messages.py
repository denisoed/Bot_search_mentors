from .button.create_button import search_mentor_btn


username = {
    'get_name': '🤵 Ну что будем знакомиться? Напиши своё имя пожалуйста',
    'unknown_message': 'Прости но ты втираешь мне какую то дичь!',
    'success_get_name': '🤵 Прекрасно!\n\n Я приготовил для тебя тут пару инструкций:\n \
    1)'
}

handler_reply_button = [
    {
        'name': 'Быстрый поиск',
        'run': search_mentor_btn,
        'text': 'Для поиска нужно указать Имя ментора'
    },
    {
        'name': 'Найти',
        'run': '',
        'text': ''
    }
]
