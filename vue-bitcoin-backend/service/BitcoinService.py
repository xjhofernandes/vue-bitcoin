from model.BitcoinValues import BitcoinValues
from repository.MongoDbAcess import MongoDbAcess

class BitcoinService(object):
    def __init__(self) -> None:
        connection = MongoDbAcess()
    
    def period_filter(self):
        return True

    def calendar_filter(self):
        return True

    def teste_db(self):
        print('tedsdste')
        print(BitcoinValues.objects.count())