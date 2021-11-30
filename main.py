import time
import schedule
from sniper.sniper import DydxData, place_order


def job():
    dydx_data = DydxData()
    z_score = dydx_data.find_z()
    place_order(z_score)


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
