import nonebot
from nonebot import NLPSession, on_natural_language, NLPResult, on_command, IntentCommand
from .wife_config import *

wife_lists = user_list()


@nonebot.scheduler.scheduled_job(
    'cron',
    day='*',
    hour='7',
    minute='30'
)
async def hunsband_goodMorning():
    bot = nonebot.get_bot()
    for i in wife_lists.all_user:
        try:
            await bot.send_private_msg(user_id=i.id, message='老公早安!')
            await bot.send_private_msg(user_id=i.id, message=get_love_scence())
        except:
            pass


def read():
    try:
        with open('index.json', 'r+', encoding='utf-8') as f:
            line = f.readline()
            while line:
                line = str(line).replace('[', '').replace(',\n', '').replace(']', '')
                t = json.loads(line)
                user_id = t['husband']
                temp_wife = wife(user_id)
                temp_wife.height = t['height']
                temp_wife.widget = t['widget']
                temp_wife.name = t['name']
                temp_wife.ouPai = t['ouPai']
                temp_wife.liking = t['liking']
                temp_wife.sex = t['sex']
                temp_wife.age = t['age']
                temp_wife.isMerry = t['isMerry']
                temp_wife.work = t['work']
                temp_wife.race = t['race']
                temp_wife.meng = t['meng']
                temp_wife.husband = t['husband']
                wife_lists.add_user(temp_wife)
                wife_lists.all_user.append(user(user_id))
                line = f.readline()
            f.close()

    except:
        with open('index.json', 'a+', encoding='utf-8') as f:
            f.close()
            return


@on_command('fuckingIndex', aliases="我的渣男值", only_to_me=False)
async def wife_self_index(session: NLPSession):
    bot = nonebot.get_bot()
    send_user = session.event['user_id']
    for i in wife_lists.all_user:
        if i.id == send_user:
            await session.send(message=str(i.fuckingBoy), at_sender=True)
            break
    else:
        await session.send(message="没有找到你的信息", at_sender=True)


@on_command('wife', aliases=('老婆'), only_to_me=False)
# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
async def _(session: NLPSession):
    if not wife_lists.alredyInit:
        read()
        wife_lists.alredyInit = True
    bot = nonebot.get_bot()
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                await session.send(message=f'我是{i.name},老公你找我啊', at_sender=True)
        return
    else:
        flag = False
        for i in wife_lists.all_user:
            if i.id == send_user and i.fuckingBoy >= 20:
                await session.send(message="你抛弃了超过20位女孩，你不配活着，去死吧渣男", at_sender=True)
                return
            elif i.id == send_user:
                flag = True
                break
        if not flag:
            wife_lists.all_user.append(user(send_user))
        tempWife = wife(send_user)
        wife_lists.add_user(tempWife)
        await session.send(message=f"你好！我是{tempWife.name},从今天开始就成为你的妻子了，请多关照", at_sender=True)
    write(wife_lists)


@on_command('wife_index', aliases="老婆的个人信息", only_to_me=False)
async def wife_self_index(session: NLPSession):
    bot = nonebot.get_bot()
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                await session.send(message=i.print_wife_index(), at_sender=True)
                return
    else:
        await session.send(message="你还没有老婆", at_sender=True)


@on_command('end', aliases="分手", only_to_me=False)
async def love(session: NLPSession):
    bot = nonebot.get_bot()
    send_user = session.event['user_id']
    for i in wife_lists.all_user:
        if i.id == send_user:
            i.fuckingBoy += 1
            break
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                if i.sex == '病娇':
                    await session.send(message=i.name + ":" + "这样啊……你不喜欢我么？那就杀死吧！ 没关系，只要在身边就可以了，无论以什么形式都可以；活着也好， "
                                                              "死掉也好，都可以。", at_sender=True)
                elif i.sex == '温柔':
                    await session.send(message=i.name + ":" + "这段时间感谢你照顾了，以后要好好吃饭，不要再熬夜了，请一定照顾好自己……", at_sender=True)
                elif i.sex == '傲娇':
                    await session.send(message=i.name + ":" + "哼，分就分，大笨蛋，我也从来就没有喜欢过你，就此别过吧……我绝对不会再想起你的，哼~永别了",
                                       at_sender=True)
                elif i.sex == '傲慢':
                    await session.send(message=i.name + ":" + "呵，愚蠢的人类，我以前居然对你这种似人非人的生物抱有爱慕，我真是愚蠢，那么祝你下地狱吧",
                                       at_sender=True)
                elif i.sex == '天真':
                    await session.send(message=i.name + ":" + "明明是我先来的~为什么……为什么你连分手都会这么熟练啊，为什么，我不懂啊！",
                                       at_sender=True)
                else:
                    await session.send(message=i.name + ":" + "祝你幸福", at_sender=True)
                wife_lists.user_wife_list.remove(i)
                wife_lists.user.remove(send_user)
                write(wife_lists)
                return
    else:
        await session.send(message="你没有老婆,谈什么分手", at_sender=True)


@on_command('wife_shit', aliases="老婆骂我", only_to_me=False)
async def wife_shit(session: NLPSession):
    send_user = session.event['user_id']
    url = 'https://v1.alapi.cn/api/soul'
    date = requests.get(url).json()['data']['title']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband==send_user:
                await session.send(i.name+':'+date, at_sender=True)
    else:await session.send(message="你没有老婆", at_sender=True)

@on_command('get_merry', aliases="结婚", only_to_me=False)
async def love(session: NLPSession):
    bot = nonebot.get_bot()
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                await session.send(message=i.name + ":" + i.get_merry(), at_sender=True)
    else:
        await session.send(message="你没有老婆,谈什么结婚", at_sender=True)


@on_command('wife_love', aliases="老婆！", only_to_me=False)
async def love(session: NLPSession):
    bot = nonebot.get_bot()
    send_user = session.event['user_id']
    if send_user in wife_lists.user:
        for i in wife_lists.user_wife_list:
            if i.husband == send_user:
                i.liking += 2
                await session.send(message=i.name + ":" + i.get_love_scence(), at_sender=True)
    else:
        await session.send(message="你没有老婆", at_sender=True)
