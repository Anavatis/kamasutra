class Message:
    def __init__(self, message="", attachment="", keyboard=""):
        self.message = message
        self.attachment = attachment
        self.keyboard = keyboard

    def get_message_dict(self):
        return dict(message=self.message,
                    attachment=self.attachment,
                    keyboard=self.keyboard)