import re
from typing import List

from hoshino import HoshinoBot, Service
from hoshino.typing import CQEvent, MessageSegment

from . import functions as fn
from .data_source import make_image
from .models import Command, UserInfo
from .download import DownloadError,ResourceError
from .utils import help_image
sv = Service("头像表情包")
commands = [
    Command(("摸", "摸摸", "rua"), fn.petpet),
    Command(("亲", "亲亲"), fn.kiss),
    Command(("贴", "贴贴", "蹭", "蹭蹭"), fn.rub),
    Command(("顶", "玩"), fn.play),
    Command(("拍",), fn.pat),
    Command(("撕",), fn.rip),
    Command(("丢", "扔"), fn.throw),
    Command(("爬",), fn.crawl),
    Command(("精神支柱",), fn.support),
    Command(("一直",), fn.always, convert=False),
    Command(("加载中",), fn.loading, convert=False),
    Command(("转",), fn.turn),
    Command(("小天使",), fn.littleangel, convert=False, arg_num=1),
    Command(("不要靠近",), fn.dont_touch),
    Command(("一样",), fn.alike),
    Command(("滚",), fn.roll),
    Command(("玩游戏", "来玩游戏"), fn.play_game, convert=False),
    Command(("膜", "膜拜"), fn.worship),
    Command(("吃",), fn.eat),
    Command(("啃",), fn.bite),
    Command(("出警",), fn.police),
    Command(("问问", "去问问"), fn.ask, convert=False, arg_num=1),
]
@sv.on_fullmatch("头像表情包")
async def help(bot:HoshinoBot,ev:CQEvent):
    im = await help_image(commands)
    await bot.send(ev,MessageSegment.image(im))
def is_qq(msg: str):
    return msg.isdigit() and 11 >= len(msg) >= 5

async def get_user_info(bot: HoshinoBot, user: UserInfo):
    if not user.qq:
        return

    if user.group:
        info = await bot.get_group_member_info(
            group_id=int(user.group), user_id=int(user.qq)
        )
        user.name = info.get("card", "") or info.get("nickname", "")
        user.gender = info.get("sex", "")
    else:
        info = await bot.get_stranger_info(user_id=int(user.qq))
        user.name = info.get("nickname", "")
        user.gender = info.get("sex", "")
async def handel(ev: CQEvent, prefix: str = ""):
    users: List[UserInfo] = []
    args: List[str] = []
    msg = ev.message
    for msg_seg in msg:
        if msg_seg.type == "at":
            users.append(UserInfo(qq=msg_seg.data["qq"], group=str(ev.group_id)))
        elif msg_seg.type == "image":
            users.append(UserInfo(img_url=msg_seg.data["url"]))
        elif msg_seg.type == "text":
            for text in str(msg_seg.data["text"]).split():
                if prefix != "":
                    text = re.sub(prefix, "", text)
                if is_qq(text):
                    users.append(UserInfo(qq=text))
                elif text == "自己":
                    users.append(UserInfo(qq=str(ev.user_id), group=str(ev.group_id)))
                else:
                    text = text.strip()
                    if text:
                        args.append(text)
    return users, args


@sv.on_prefix(("/","pp/"))
async def gen_image(bot: HoshinoBot, ev: CQEvent):
    msg = ev.message.extract_plain_text().strip()
    assert isinstance(msg, str)
    for com in commands:
        for kw in com.keywords:
            if kw in msg:
                args = msg[len(kw) :]
                users, args = await handel(ev, kw)
                sender = UserInfo(qq=str(ev.user_id))
                await get_user_info(bot, sender)
                for user in users:
                    await get_user_info(bot, user)
                try:
                    im = await make_image(com, sender, users, args=args)
                except DownloadError:
                    await bot.finish(ev,"图片下载出错，请稍后再试")
                except ResourceError:
                    await bot.finish(ev,"资源下载出错，请稍后再试")
                except:
                    # logger.warning(traceback.format_exc())
                    await bot.finish(ev,"出错了，请稍后再试")
                if "base64" in im:
                    im = MessageSegment.image(im)
                await bot.send(ev, im)
