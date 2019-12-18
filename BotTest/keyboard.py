import json


class Keyboard:

    def __init__(self, bool):
        self.bool = bool
        self.buttons = []

    def add_button(self, label, color, payload=""):
        self.buttons.append([{
            "action": {
                "type": "text",
                "payload": json.dumps(payload),
                "label": label
            },
            "color": color}])

    def get_keyboard(self):
        return {
            "one_time": self.bool,
            "buttons": self.buttons
        }

    def get(self):
        return str(json.dumps(self.get_keyboard(), ensure_ascii=False))
