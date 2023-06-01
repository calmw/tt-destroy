import os
from log import logger
import schedule
from task.task import burnTt, destroyTt

currPath = os.path.dirname(os.path.abspath(__file__))
logFile = "{}/log/logs.log".format(currPath)
logger.config_log(logFile)

schedule.every(5).minutes.do(destroyTt)
schedule.every().day.at("08:00").do(burnTt)
schedule.run_all()  # 正式服屏蔽掉-------------------------------------

while True:
    schedule.run_pending()
