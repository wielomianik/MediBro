from service.search import SearchForVisit
from module.config import MediConf
from service.telegram import MediBot
from bs4 import BeautifulSoup


if __name__ == '__main__':
    engine = SearchForVisit()
    config = MediConf()

    engine.login()
    appointments_list = engine.search()

    results = []
    if appointments_list:
        for app in appointments_list:
            soup = BeautifulSoup(app, 'html.parser')
            results.append([
                soup.find(class_=config.app_time).get_text(strip=True),
                soup.find(class_=config.app_localization).get_text(strip=True),
                soup.find(class_=config.app_doctor).get_text(strip=True)
            ])

    medibot = MediBot()
    for result in results:
        medibot.send_notification(result)
