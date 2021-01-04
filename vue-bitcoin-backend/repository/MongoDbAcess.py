from mongoengine import connect

class MongoDbAcess(object):
    def __init__(self) -> None:
        connect('bitcoin')
        #connect('bitcoin', host='cluster0.oyaw3.mongodb.net', username='admin', password='bitadmin', authentication_source='admin')
