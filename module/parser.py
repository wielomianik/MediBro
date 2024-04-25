from bs4 import BeautifulSoup
from module.config import MediConf


class MediParser:

    def __init__(self):
        self.result = []
        self.soup = None
        self.config = MediConf()

    def parse_inner_html(self, content: list) -> list:
        if content:
            for element in content:
                self.soup = BeautifulSoup(element, 'html.parser')
                self.result.append([
                    self.soup.find(class_=self.config.app_time).get_text(strip=True),
                    self.soup.find(class_=self.config.app_localization).get_text(strip=True),
                    self.soup.find(class_=self.config.app_doctor).get_text(strip=True)
                ])
        return self.result
