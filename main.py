import os
from log import logger
import schedule as schedule
from task.task import destroy_tt

currPath = os.path.dirname(os.path.abspath(__file__))
logFile = "{}/log/logs.log".format(currPath)
logger.config_log(logFile)

schedule.every(5).minutes.do(destroy_tt)
schedule.run_all()

while True:
    schedule.run_pending()
