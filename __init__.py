"""发送 头像表情包 获取帮助 指令为 pp 或 /"""
import re
import traceback
from typing import List, Tuple

from botoy import GroupMsg, S, logger
from botoy.async_decorators import equal_content, ignore_botself
from botoy.collection import MsgTypes
from botoy.contrib import plugin_receiver
from botoy.parser import group as gp

from .data_source import commands, make_image
from .download import DownloadError, ResourceError
from .models import UserInfo
from .utils import help_image


@plugin_receiver.group
@ignore_botself
@equal_content("头像表情包")
async def help(ctx):
    im = await help_image(commands)
    if im.startswith("base64://"):
        im = im[9:]
    await S.bind(ctx).aimage(im, type=S.TYPE_BASE64)


def is_qq(msg: str):
    return msg.isdigit() and 11 >= len(msg) >= 5


# TODO: user.name, user.gender
async def get_user_info(ctx: GroupMsg, user: UserInfo):
    if not user.qq:
        return

    return
    #
    # if user.group:
    #     info = await bot.get_group_member_info(
    #         group_id=int(user.group), user_id=int(user.qq)
    #     )
    #     user.name = info.get("card", "") or info.get("nickname", "")
    #     user.gender = info.get("sex", "")
    # else:
    #     info = await bot.get_stranger_info(user_id=int(user.qq))
    #     user.name = info.get("nickname", "")
    #     user.gender = info.get("sex", "")


async def handle(ctx: GroupMsg, prefix: str = "") -> Tuple[List[UserInfo], List[str]]:
    users: List[UserInfo] = []
    args: List[str] = []
    text = ""

    # opq没有消息段的概念，吐血

    if ctx.MsgType == MsgTypes.AtMsg:
        at_data = gp.at(ctx)
        assert at_data
        qq = at_data.UserID[0]
        group = ctx.FromGroupId
        users.append(UserInfo(qq=str(qq), group=str(group)))
        text = ctx.Content
    elif ctx.MsgType == MsgTypes.PicMsg:
        pic_data = gp.pic(ctx)
        assert pic_data
        if pic_data.UserID:
            users.append(
                UserInfo(qq=str(pic_data.UserID[0]), group=str(ctx.FromGroupId))
            )
        users.append(UserInfo(img_url=pic_data.GroupPic[0].Url))
        text = pic_data.Content
    elif ctx.MsgType == MsgTypes.TextMsg:
        text = ctx.Content

    # 去除指令
    text = text.strip("/").strip("pp")

    for text in text.split():
        if prefix != "":
            text = re.sub(prefix, "", text)
        if is_qq(text):
            users.append(UserInfo(qq=text))
        elif text == "自己":
            users.append(UserInfo(qq=str(ctx.FromUserId), group=str(ctx.FromGroupId)))
        else:
            text = text.strip()
            if text:
                args.append(text)

    return users, args


@plugin_receiver.group
@ignore_botself
async def gen_image(ctx: GroupMsg):
    # 不想处理回复了
    if gp.reply(ctx):
        return
    if ctx.MsgType == MsgTypes.AtMsg:
        msg = gp.at(ctx).Content  # type: ignore
    elif ctx.MsgType == MsgTypes.PicMsg:
        msg = gp.pic(ctx).Content  # type: ignore
    elif ctx.MsgType == MsgTypes.TextMsg:
        msg = ctx.Content
    else:
        return

    if not msg.startswith("pp") and not msg.startswith("/"):
        return
    msg = msg.strip("/").strip("pp")

    for cmd in commands:
        for kw in cmd.keywords:
            if kw in msg:
                args = msg[len(kw) :]
                users, args = await handle(ctx, kw)
                sender = UserInfo(qq=str(ctx.FromUserId))
                await get_user_info(ctx, sender)
                for user in users:
                    await get_user_info(ctx, user)
                # 能跑就行：）
                if not users:
                    users.append(sender)

                try:
                    im = await make_image(cmd, sender, users, args=args)
                except DownloadError:
                    await S.atext("图片下载出错，请稍后再试")
                except ResourceError:
                    await S.atext("资源下载出错，请稍后再试")
                except:
                    logger.warning(traceback.format_exc())
                    await S.atext("出错了，请稍后再试")
                else:
                    if isinstance(im, str) and im.startswith("base64://"):
                        im = im[9:]
                    await S.aimage(im)

                return
