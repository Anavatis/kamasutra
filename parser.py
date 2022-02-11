from random import randint

import requests
from bs4 import BeautifulSoup

import utils
import vkapi
from message import Message

site = "https://medow.club/pozy"


class KamasutraParser:

    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")

    def get_pose_info(self):
        title = self.get_title()
        description = self.get_description()
        image_link = self.get_image_link()
        image_data = self.get_image_data(image_link)
        return dict(
            title=title,
            description=description,
            image=image_data)

    def get_title(self):
        title = self.soup.find("h1", class_="entry-title")
        return title.text

    def get_description(self):
        description = self.soup.find("p")
        return description.text

    def get_image_link(self):
        image = self.soup.find("img", class_="attachment-full")
        return image.get('src')

    @staticmethod
    def get_image_data(image):
        image_data = requests.get(image)
        return image_data.content


def get_message_from_pose_info(pose_info: dict) -> Message:
    title = pose_info.get('title', 'Ошибка названия')
    description = pose_info.get('description', 'Нет описания')

    photo = vkapi.upload_photo(pose_info.get("image"))

    return Message(message=f'{title}\n\n{description}',
                   attachment=photo,
                   keyboard=utils.get_keyboard('default_keyboard'))


def get_random_pose():
    random_pose_number = randint(1, 490)
    url = f'{site}/poza-{random_pose_number}.html'
    parser = KamasutraParser(url)
    pose_info = parser.get_pose_info()
    message = get_message_from_pose_info(pose_info)
    return message

