import requests
from module.config import MediConf


class MediBot:

    def __init__(self):
        self.config = MediConf()
        self.url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(
            self.config.telegram_token,
            self.config.telegram_chat_id
        )

    def send_notification(self, content: str = None):
        requests.get(self.url + '&text={}'.format(content))
