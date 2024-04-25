from module.parser import MediParser
from service.medicover import MediCover
from service.medibot import MediBot
from traceback import format_exc


if __name__ == '__main__':
    medicover = MediCover()
    medibot = MediBot()
    mediparser = MediParser()

    try:
        medicover.login()
        result = medicover.search()
        if result:
            for element in mediparser.parse_inner_html(medicover.search()):
                medibot.send_notification("Wizyta: {}, {}, {}".format(*element))
        else:
            print("Brak wizyt...")

    except Exception:
        medibot.send_notification(format_exc())
        medicover.close()
        raise

    medicover.close()
