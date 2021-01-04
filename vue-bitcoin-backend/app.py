from repository import MongoDbAcess
from model import BitcoinValues
from mongoengine import connect


connect('bitcoin')

for te in BitcoinValues.BitcoinValues.objects:
    print(te)

