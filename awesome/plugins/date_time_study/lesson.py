from  datetime import  datetime
from apscheduler.triggers.cron import CronTrigger
import nonebot
import pytz
from nonebot import on_command, scheduler
from aiocqhttp.exceptions import Error as CQHttpError

from awesome.plugins.date_time_study.config import GROUP_ID
async def high_math():
    bot=nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家准备上高数要并记得签到和完成任务点！')
    except CQHttpError:
        pass
async def english():
    bot = nonebot.get_bot()
    now = datetime.today().hour+datetime.today().minute
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家准备上英语并前往英语学习群查看老师下布置得任务！')
    except CQHttpError:
        pass
async def Physical():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家准备上大学物理并记得课后上传笔记！')
    except CQHttpError:
        pass
async def Occupational():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家前往知道智慧树观看大学生职业发展与就业指导！')
    except CQHttpError:
        pass
async def sports():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家准备上体育课并打卡签到！')
    except CQHttpError:
        pass
async def Business():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家去钉钉或mooc上创业基础课！')
    except CQHttpError:
        pass
async def Li_San():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家马上去钉钉上离散数学，记得签到！')
    except CQHttpError:
        pass
async def heart():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家去知道智慧树观看大学生实用心理学！')
    except CQHttpError:
        pass
async def english_listening():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家准备上听力课！\n如果处于单周请忽略本条消息')
    except CQHttpError:
        pass
async def c_design():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家去腾讯课堂上c++并记得签到！\n+https://ke.qq.com/webcourse/index.html#cid=524712&term_id=100622221&taid=4265070029177256&from=41')
    except CQHttpError:
        pass
async def history():
    bot = nonebot.get_bot()
    now = str(datetime.today().hour)+':'+str(datetime.today().minute)
    try:
        await bot.send_group_msg(group_id=GROUP_ID, message=f'现在已经{now}点啦，请大家去学习通上中国近现代史纲要！')
    except CQHttpError:
        pass