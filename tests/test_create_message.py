import unittest
from assets.message import create_message


class TestCreateMessage(unittest.TestCase):

    def test_create_mentor_card(self):
        data = ['John', 'Doe', 'python', 'javascript, python', '@maddevsio']
        ready_mentor_card = '''
<strong>John Doe</strong> \n
Основной язык: <strong>python</strong> 
Дополнительные языки: <strong>javascript, python</strong>
Ссылка на телеграм: <a href="@maddevsio">@maddevsio</a>
'''
        self.assertEqual(create_message.create_mentor_card(data), ready_mentor_card)

    def test_create_question_card(self):
        data = {'name': 'John', 'title': 'Test problem', 'question': 'Not working test', 'lang': 'python'}
        question = '''
Здравствуйте! Меня John зовут. \n
Я извиняюсь если отвлекаю Вас,
но если есть свободная минутка помогите пожалуйста \n
В общем суть проблемы: Test problem \n
Краткое описание вопроса: Not working test \n
Дополнительная информация!
Основной язык на котором ведется разработка: python
    '''
        self.assertEqual(create_message.question_card(data), question)

    def test_create_mentors_card(self):
        data = [['John', 'Doe', 'python', 'javascript, python', '@maddevsio']]
        card = '▫️ John Doe \n Основной язык: python\n Дополнительные языки: javascript, python\n Ссылка: @maddevsio\n\n'
        self.assertEqual(create_message.mentors_card(data), card)