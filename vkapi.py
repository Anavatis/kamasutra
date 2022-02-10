import os
import random

import requests
import vk as vk

from message import Message


session = vk.Session()
api = vk.API(session=session, v=5.131)
access_token = os.environ.get("ACCESS_TOKEN")


def send_message(peer_id, message: Message):
    api.messages.send(access_token=access_token,
                      peer_id=peer_id,
                      random_id=random.randint(-2 ** 10, 2 ** 10),
                      dont_parse_links=True,
                      **message.get_message_dict())


def upload_photo(photo):
    upload_data = api.photos.getMessagesUploadServer(group_id=os.environ.get("GROUP_ID"),
                                                     access_token=access_token)
    upload_url = upload_data.get('upload_url')
    r = requests.post(url=upload_url, files={'photo': ('kamasimage.png', photo, 'image/png')})
    photo_data = r.json()
    photo = api.photos.saveMessagesPhoto(access_token=access_token,
                                         photo=photo_data.get('photo'),
                                         server=photo_data.get('server'),
                                         hash=photo_data.get('hash'))[0]

    return f'photo{photo["owner_id"]}_{photo["id"]}'
