from api import YandexDisk
from unittest import TestCase

ya_client = YandexDisk()


class TestApi(TestCase):
    def test_folder_created(self):
        expected = 'Папка успешно создана'
        res = ya_client.create_folder('netology')
        self.assertEquals(res, expected, 'Папка уже создана')
        print(res)

    def test_folder_already_exists(self):
        expected = 'Папка уже существует'
        res = ya_client.create_folder('netology')
        self.assertEquals(res, expected)
        print(res)

    def test_cannot_create_folder(self):
        expected = 'Не удалось создать папку на сервере'
        res = ya_client.create_folder('netology')
        self.assertEquals(res, expected, 'Не удалось создать папку')
        print(res)
