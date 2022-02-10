def get_keyboard(keyboard_name):
    """ Return non-json-format keyboard """
    path_to_keyboards_dir = 'keyboards/'
    path_to_keyboard_file = path_to_keyboards_dir + keyboard_name + '.json'

    with open(path_to_keyboard_file, 'r', encoding='utf-8') as file:
        keyboard = file.read()

    return keyboard
