# fileName : plugins/dm/commands.py
# copyright ÂŠī¸ 2021 nabilanavab

# LOGGING INFO: DEBUG
import logging
logger=logging.getLogger(__name__)
logging.basicConfig(
                   level=logging.DEBUG,
                   format="%(levelname)s:%(name)s:%(message)s" # %(asctime)s:
                   )

import os
import shutil
from pdf import PDF
from pdf import PROCESS
from asyncio import sleep
from pyrogram import filters
from configs.dm import Config
from configs.images import FEEDBACK
from pyrogram import Client as ILovePDF


feedbackMsg=f"[Write a feedback đ]({FEEDBACK})"

userHELP="""[USER COMMAND MESSAGES]:\n
/start, /ping: to check whether Bot alive\n
/help, /command: for this message\n
/generate: generate PDF with current images\n
/delete: deletes the current image to pdf queue\n
/txt2pdf: to create pdf files from text message\n
/feedback: to Write something about TG PDF CONVERTER BOT"""

adminHelp="""\n\n[ADMIN COMMAND MESSAGES]:\n
/server: to get current bot, server status\n
/ban `id/usrnm`: to ban a user\n
/unban `id/usrnm`: to unban a banned user\n
/deleteUser `id/usrnm`: delete user from database\n
/forward `id/usrnm`: replied message forward to user\n
/forward c `id/usrnm`: replied message forward as copy\n
/users: get current bot users list\n
/broadcast: replied message broadcast to all users\n
/broadcast f: replied message forward to bot users"""

footer="""\n\nSource-Code: [TG PDF CONVERTER](https://t.me/DeltaBotsOfficial)\n
Bot: @tgPDFconverterBOT đ\n
[Support Channel](https://t.me/DeltaBotsOfficial)"""


# â CANCELS CURRENT PDF TO IMAGES WORK â
@ILovePDF.on_message(
                    (filters.private | filters.group) &
                    filters.command(["cancel"]) &
                    filters.incoming
                    )
async def cancelP2I(bot, message):
    try:
        PROCESS.remove(message.from_user.id)
        await message.delete()          # delete /cancel if process canceled
    except Exception:
        try:
            await message.reply_chat_action(
                                           "typing"
                                           )
            await message.reply_text(
                                    'đ¤', quote = True
                                    )
        except Exception:
            pass

# â DELETS CURRENT IMAGES TO PDF QUEUE (/delete) â
@ILovePDF.on_message(
                    (filters.private | filters.group) &
                    filters.command(["delete"]) &
                    filters.incoming
                    )
async def _cancelI2P(bot, message):
    try:
        await message.reply_chat_action(
                                       "typing"
                                       )
        del PDF[message.chat.id]
        await message.reply_text(
                                "`Queue deleted Successfully..`đ¤§",
                                quote = True
                                )
        shutil.rmtree(f"{message.chat.id}")
    except Exception:
        await message.reply_text(
                                "`No Queue founded..`đ˛",
                                quote = True
                                )

# â GET USER ID (/id) â
@ILovePDF.on_message(
                    (filters.private | filters.group) &
                    filters.command(["id"]) &
                    filters.incoming
                    )
async def userId(bot, message):
    try:
        if message.chat.id == message.from_user.id:
            await message.reply_text(
                                    f"**Your Name** : {message.from_user.mention}\n"
                                    f"**Id** : `{message.chat.id}`",
                                    quote = True
                                    )
        else:
            await message.reply_text(
                                    f"**Chat Title**    : `{message.chat.title}`\n"
                                    f"**User Name** : `{message.from_user.mention}`\n"
                                    f"**Chat ID**        : `{message.chat.id}`\n"
                                    f"**User ID**        : `{message.from_user.id}`",
                                    quote = True
                                    )
    except Exception as e:
        logger.exception(
                        "/ID:CAUSES %(e)s ERROR",
                        exc_info=True
                        )


# â GET FEEDBACK MESSAGE â
@ILovePDF.on_message(
                    (filters.private | filters.group) &
                    filters.command(["feedback"]) &
                    filters.incoming
                    )
async def feedback(bot, message):
    try:
        await message.reply_text(
                                feedbackMsg,
                                disable_web_page_preview = True
                                )
    except Exception as e:
        logger.exception(
                        "/FEEDBACK:CAUSES %(e)s ERROR",
                        exc_info = True
                        )

# â DELETS CURRENT IMAGES TO PDF QUEUE (/delete) â
@ILovePDF.on_message(
                    (filters.private | filters.group) &
                    filters.command(["help", "commands"]) &
                    filters.incoming)
async def _help(bot, message):
    try:
        await message.reply_chat_action(
                                       "typing"
                                       )
        helpMsg = await message.reply(
                                     "âī¸ Processing..",
                                     quote = True
                                     )
        await sleep(2)
        HELP = userHELP
        await helpMsg.edit(
                          HELP
                          )
        if message.from_user.id in Config.ADMINS:
            await sleep(4)
            HELP = userHELP + adminHelp
            await helpMsg.edit(
                              HELP
                              )
        await sleep(2)
        HELP += footer
        await helpMsg.edit(
                          HELP,
                          disable_web_page_preview = True)
    except Exception as e:
        logger.exception(
                        "/HELP:CAUSES %(e)s ERROR",
                        exc_info=True
                        )

#                                                                                  Telegram: @DeltaBotsOfficial
