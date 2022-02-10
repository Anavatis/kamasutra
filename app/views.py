import os

from flask import request, json, Blueprint, render_template

import handler

kamasutra = Blueprint('kamasutra', __name__, url_prefix='/')


@kamasutra.route('/')
def test_index():
    return render_template('index.html')


@kamasutra.route('/callback/vk', methods=["POST"])
def processing():
    data = json.loads(request.data)

    if 'type' not in data:
        return 'not vk'

    if data['type'] == 'confirmation':
        return os.environ.get("CONFIRMATION_TOKEN")
    elif data['type'] == 'message_new':
        handler.get_answer(data['object']['message'])

    return 'ok'
