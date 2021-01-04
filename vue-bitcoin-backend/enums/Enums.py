from enum import Enum
from datetime import date

class Periods(Enum):
   seven = 7
   month = 30
   sixmonth = 180
   year = 360
   max = 9999