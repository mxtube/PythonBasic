"""
Lesson 39 - Parser class
10.05.2023 @ Kirill Kuznetsov
"""

from bs4 import BeautifulSoup
import urllib.request


class Parser:

    raw_html = ''
    html = ''
    result = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        teachers = self.html.find_all('div', class_='teacherblock')
        for teacher in teachers:
            title = teacher.find('a', class_='fio').get_text(strip=True)
            if teacher.find('img', class_='photo_teacher'):
                photo = 'https://kp11.mskobr.ru' + teacher.find('img', class_='photo_teacher')['src']
            else:
                photo = 'Нет фото'
            job_title = teacher.find('div', class_='subject').get_text(strip=True)
            self.result.append({
                'title': title,
                'photo_url': photo,
                'job_title': job_title
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.result:
                f.write(f'Преподаватель: №{i}\n\nФИО: {item["title"]}\nДолжность: {item["job_title"]}\nФото: {item["photo_url"]}\n\n*******************\n\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
