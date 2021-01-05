from service.BitcoinService import BitcoinService
from model.RequestBody import RequestBody
from enums.Enums import Periods
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


# teste = BitcoinService()

# nome = 'seven'
# print(Periods[nome].value)

# # print(teste.calendar_filter(datetime.datetime(2020, 12, 1), datetime.datetime(2020, 12, 31)))

# caramba = teste.period_filter(Periods[nome].value)
# print(caramba)
app = FastAPI()
bit_service = BitcoinService()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/updateChart/")
async def update_chart(request: RequestBody):
    result = bit_service.period_filter(Periods[request.period])
    return result


@app.post("/updateChartByCalendar/")
async def update_chart_by_calendar(request: RequestBody):
    return result