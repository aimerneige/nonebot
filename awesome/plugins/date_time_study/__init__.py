from datetime import datetime
from apscheduler.triggers.cron import CronTrigger
import nonebot
import pytz
from nonebot import on_command, scheduler
from aiocqhttp.exceptions import Error as CQHttpError
from awesome.plugins.date_time_study.config import GROUP_ID
from .mon import *


@nonebot.scheduler.scheduled_job(
    'interval',
    minutes=10,
)
async def _():
    d = datetime.today().weekday()
    try:
        if 0 <= d <=5:
            print(d)
            try:
                await mon(d)
            except:
                return
    except:
        return
