from .button import create_button
from .message import create_message
from . import main

message_instruction = {
    'get_name': '🤵 Начнем!',
    'unknown_message': 'Прости но ты втираешь мне какую то дичь!',
    'success_get_name': '''
🤵 Привет! Я бот для поиска менторов \n
Я помогу найти нужного ментора,
для этого тебе нужно воспользоваться кнопкой "Быстрый поиск"!\n
А если ты новичок и не знаешь что делать
можешь нажать на кнопку "Помочь"
где тебе предстоит ответить на несколько легких вопросов
с которых сформируется сообщение для ментора
Тебе не придется долго расписывать свою проблему
ведь для этого у тебя есть Я!   
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
        'run': create_button.start_create_question,
        'text': '''
❗️Хорошо поставленный вопрос — тот, 
на который участник деловой беседы захочет ответить, 
сможет ответить или над которым ему захочется подумать.
'''        
    },
    {
        'name': 'Начать',
        'run': create_button.help_slide_btn,
        'text': 'Ну для начала нужно указать как тебя зовут'
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
        'run': main.creating_question,
        'text': 'Продолжим'
    }
]

handler_inline_button = [
    {
        'name': 'yet',
        'run': main.get_all_mentors,
        'text': 'yet'
    }
]

question_data = {
    'name': '',
    'title': 'Опиши в двух словах суть проблемы(например "Падают тесты")',
    'the_problem': 'Опишите коротко свой вопрос',
    'lang': 'Основной язык',
    'done': 'Вопрос готов!'
}

message_handler_db = {
    'not_name_and_surname': 'Ментор с таким Именем и Фамилией не найден!',
    'not_name_or_surname': 'Ментор с таким Именем или Фамилией не найден!',
    'not_correct': 'Пожалуйста введите корректные данные',
    'is_empty': 'Введите данные'
}
