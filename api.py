import requests


class YandexDisk:
    token = ''

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        return href

    def create_folder(self, folder_name):
        """Метод для создания папки на Яндекс диске"""
        headers = self.get_headers()
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {'path': folder_name}

        is_folder_exists_req = requests.get(url, headers=headers, params=params)

        print(is_folder_exists_req.status_code)

        if is_folder_exists_req.status_code != 200:
            create_folder_req = requests.put(url, headers=headers, params=params)

            if create_folder_req != 200:
                return 'Не удалось создать папку на сервере'

            return 'Папка успешно создана'
        else:
            return 'Папка уже существует'
