"""Command To Check Bot is Alive or Not
.you_live"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("you_live"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Zinda Hu Sir \n\nUser Bot version: 1.9.0\nPython: 3.7.3\nBot Owner: @XHACKERKUNAL\nJON @EONARMY TO GET PREMIUM ACCOUNT LIKE NETFLIX,HOTSTAR,AMAZON PRIME AND ETC...!`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
