from service.BitcoinService import BitcoinService
from enums.Enums import Periods

teste = BitcoinService()

nome = 'seven'
print(Periods[nome].value)

# print(teste.calendar_filter(datetime.datetime(2020, 12, 1), datetime.datetime(2020, 12, 31)))

caramba = teste.period_filter(Periods[nome].value)
print(caramba)