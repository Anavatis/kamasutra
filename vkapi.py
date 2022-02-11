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


def get_upload_server_url():
    upload_server = api.photos.getMessagesUploadServer(group_id=os.environ.get("GROUP_ID"),
                                                       access_token=access_token)
    print(upload_server)
    return upload_server['upload_url']


def get_photo_data(upload_url, photo):
    r = requests.post(url=upload_url, files={'photo': ('kamasimage.png', photo, 'image/png')})
    return r.json()


def upload_photo(photo):
    upload_url = get_upload_server_url()
    photo_data = get_photo_data(upload_url, photo)
    photo = api.photos.saveMessagesPhoto(access_token=access_token,
                                         photo=photo_data.get('photo'),
                                         server=photo_data.get('server'),
                                         hash=photo_data.get('hash'))[0]

    return f'photo{photo["owner_id"]}_{photo["id"]}'
