from service.search import SearchForVisit


if __name__ == '__main__':
    engine = SearchForVisit()
    engine.login()
    engine.search()
