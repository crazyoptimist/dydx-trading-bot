import time
import schedule
from sniper.sniper import job


schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# job()
