from model import BitcoinValues
from repository import MongoDbAcess

connection = MongoDbAcess.MongoDbAcess()

print(BitcoinValues.BitcoinValues.objects.count())

def period_filter():
    return True



