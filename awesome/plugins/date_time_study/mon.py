from datetime import datetime
from apscheduler.triggers.cron import CronTrigger
import nonebot
import pytz
from nonebot import on_command, scheduler
from aiocqhttp.exceptions import Error as CQHttpError
from .lesson import *
from awesome.plugins.date_time_study.config import *



async def mon():
    bot=nonebot.get_bot()
    today = datetime.today()
    time = today.hour
    minutes = today.minute
    switch_three = {7: high_math, 9: english, 15: Physical}
    switch_six = {7: high_math, 13: Physical, 15: Business}
    print('执行今日任务')
    if START_LESSON <= minutes <= END_LESSON:
        try:
            print('执行今日课程')
            await switch_three[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'三班注意')
        except:
            print("三班无课")
        try:
            await switch_six[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'六班注意')
        except:
            print("六班无课")


async def tue():
    bot=nonebot.get_bot()
    today = datetime.today()
    time = today.hour
    minutes = today.minute
    switch_three = {7: history, 9: Li_San, 13: Occupational, 18: c_design}
    switch_six = {7: high_math, 9: heart, 13: english}
    print('执行今日任务')
    if START_LESSON <= minutes <= END_LESSON:
        try:
            print('执行今日课程')
            await switch_three[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'三班注意')
        except:
            print("三班无课")
        try:
            await switch_six[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'六班注意')
        except:
            print("六班无课")


async def web():
    bot = nonebot.get_bot()
    today = datetime.today()
    time = today.hour
    minutes = today.minute
    switch_three = {7: high_math, 9: english, 13: Business,15:sports}
    switch_six = {7: high_math, 13: history}
    print('执行今日任务')
    if START_LESSON <= minutes <= END_LESSON:
        try:
            print("执行今日课程")
            await switch_three[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'三班注意')
        except:
            print("三班无课")
        try:
            await switch_six[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'六班注意')
        except:
            print("六班无课")


async def thu():
    bot = nonebot.get_bot()
    today = datetime.today()
    time = today.hour
    bot=nonebot.get_bot()
    minutes = today.minute
    switch_three = {7: Li_San, 9: history, 13: Physical, 15: heart, 18: c_design}
    switch_six = {7: Li_San, 13: english, 15: english_listening}
    print('执行今日任务')
    if START_LESSON <= minutes <= END_LESSON:
        try:
            print("执行今日课程")
            await switch_three[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'三班注意')
        except:
            print("三班无课")
        try:
            await switch_six[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'六班注意')
        except:
            print("六班无课")


async def fri():
    bot = nonebot.get_bot()
    today = datetime.today()
    time = today.hour
    minutes = today.minute
    switch_three = {9: english_listening, 13: high_math}
    switch_six = {7: history, 9: Occupational, 13: high_math, 15: Physical, 18: c_design}
    print('执行今日任务')
    if START_LESSON <= minutes <= END_LESSON:
        try:
            print("执行今日课程")
            await switch_three[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'三班注意')
        except:
            print("三班无课")
        try:
            await switch_six[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'六班注意')
        except:
            print("六班无课")


async def sat():
    bot = nonebot.get_bot()
    today = datetime.today()
    time = today.hour
    minutes = today.minute
    switch_six = {18: c_design}
    try:
        if START_LESSON <= minutes <= END_LESSON:
            await switch_six[time]()
            await bot.send_group_msg(group_id=GROUP_ID, message=f'六班注意')
    except:
        return
