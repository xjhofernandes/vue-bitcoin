from model.BitcoinValues import BitcoinValues
from repository.MongoDbAcess import MongoDbAcess
from mongoengine import Q
import datetime

class BitcoinService(object):
    def __init__(self) -> None:
        connection = MongoDbAcess()
    
    def period_filter(self):
        return True

    def calendar_filter(self, start, end):
        # start = datetime.datetime(2020, 12, 1)
        # end = datetime.datetime(2020, 12, 31)
        results = BitcoinValues.objects.filter((Q(date__gte=start) & Q(date__lte=end)))
        return results.to_json()

    def teste_db(self):
        print('tedsdste')
        print(BitcoinValues.objects.count())