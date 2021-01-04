from mongoengine import *
import datetime

class BitcoinValues(Document):
    closing = FloatField()
    date = DateTimeField(default=datetime.datetime.utcnow)

    def to_json(self):
        return {
            "closing" : self.closing,
            "date" : self.date
        }
            