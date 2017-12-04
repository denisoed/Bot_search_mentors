import unittest
from assets import main

class TestMain(unittest.TestCase):

    def test_get_prev(self):
        data = ['question', 'name', 'title', 'lang']
        bot = {'bot': 'bot'}
        update = {'update': 'update'}
        self.assertTrue(main.get_prev(bot, update, 0, 'Hello'))
