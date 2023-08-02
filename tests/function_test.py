from functions import uniq_names, top_names, duration
from unittest import TestCase


class TestNames1(TestCase):
    def test_1(self):
        expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
        res = top_names()
        self.assertEquals(res, expected)


class TestNames2(TestCase):
    def test_2(self):
        expected = 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий,' \
                   ' Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл,' \
                   ' Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна,' \
                   ' Тимур, Филипп, Эдгар, Юрий'
        res = uniq_names()
        self.assertEquals(res, expected)


class TestDuration(TestCase):
    def test_3(self):
        expected = 'Fullstack-разработчик на Python - 12 месяцев, ' \
                   'Python-разработчик с нуля - 14 месяцев, ' \
                   'Java-разработчик с нуля - 20 месяцев, ' \
                   'Frontend-разработчик с нуля - 20 месяцев'
        res = duration()
        self.assertEquals(res, expected)
