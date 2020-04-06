import json
from datetime import datetime
from apscheduler.triggers.cron import CronTrigger
import nonebot
import pytz
from nonebot import on_command, scheduler
from aiocqhttp.exceptions import Error as CQHttpError
from .lesson import *
from awesome.plugins.date_time_study.config import *
from .lessons_index import *


async def send_command(class_name):
    bot = nonebot.get_bot()
    for i in GROUP_ID:
        await bot.send_group_msg(group_id=i, message=class_name + f'班注意')


async def mon(week):
    lesson_dict_three = {
        0: mon_switch_three,
        1: tue_switch_three,
        2: web_switch_three,
        3: web_switch_three,
        4: fri_switch_three}
    lesson_dict_six = {
        0: mon_switch_six,
        1: tue_switch_six,
        2: web_switch_six,
        3: web_switch_six,
        4: fri_switch_six,
        5: sat_switch_six
    }
    today = datetime.today()
    time = today.hour
    minutes = today.minute
    print('执行今日任务')
    if START_LESSON <= minutes <= END_LESSON:
        print('执行今日课程')
        try:
            clas_name = lesson_dict_three[week][time]
            b = three_teach[clas_name]
            await send_command('3')
            await send_class(clas_name, b)
        except:
            print("三班无课")
        try:
            clas_name = lesson_dict_six[week][time]
            b = three_teach[clas_name]
            await send_command('6')
            await send_class(clas_name, b)
        except:
            print("六班无课")
