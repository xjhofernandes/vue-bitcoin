from model import BitcoinValues
from mongoengine import connect

connection = connect('bitcoin', host="mongodb+srv://admin:bitadmin@cluster0.oyaw3.mongodb.net/bitcoin?retryWrites=true&w=majority")
a = connection.get_database('bitcoin').list_collection_names()

print(BitcoinValues.BitcoinValues.objects.count())
print(BitcoinValues.BitcoinValues.objects.to_json())


print(a)

