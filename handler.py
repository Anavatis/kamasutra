import utils
import vkapi
from message import Message
from parser import get_random_pose


def create_answer(message_object) -> Message:

    if message_object['text'].lower() == 'случайная поза':
        return get_random_pose()

    return Message(message="ok",
                   keyboard=utils.get_keyboard('default_keyboard'))


def get_answer(message_object: dict):
    answer = create_answer(message_object)
    user_id = message_object['from_id']
    vkapi.send_message(peer_id=user_id,
                       message=answer)
