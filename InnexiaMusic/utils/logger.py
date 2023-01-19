from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from InnexiaMusic import app
from InnexiaMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "PRIVATE CHAT"
        logger_text = f"""
**{MUSIC_BOT_NAME} PLAY LOG**
**CHAT:** {message.chat.title} [`{message.chat.id}`]
**USER:** {message.from_user.mention}
**USERNAME:** @{message.from_user.username}
**ID:** `{message.from_user.id}`
**CHAT LINK:** {chatusername}
**SEARCHED FOR:** {message.text}
**STREAM TYPE:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
