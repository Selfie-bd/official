from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, CallbackQuery
import os


ajvad = Client(
    "Pyrogram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
)

START_TEXT = """<b>Hᴇʟʟᴏ 👋 {},

Tʜɪs Is A Oꜰꜰɪᴄɪᴀʟ Bᴏᴛ Oꜰ Aɪᴏᴍ©

Yᴏᴜ Cᴀɴ Usᴇ Tʜɪs Bᴏᴛ Tᴏ Kɴᴏᴡ Mᴏʀᴇ Aʙᴏᴜᴛ Aɪᴏᴍ Cᴏᴍᴘᴀɴʏ

Yᴏᴜ Cᴀɴ Aʟsᴏ Jᴏɪɴ Oᴜʀ Tᴇᴀᴍᴇ Aɴᴅ Hɪʀᴇ Us Tᴏ Mᴀᴋᴇ Bᴏᴛs</b>"""

START_BUTTONS = [[
                InlineKeyboardButton("Jᴏɪɴ Oᴜʀ Tᴇᴀᴍ", callback_data="join")
                ]]
JOIN_BUTTON = [[
              InlineKeyboardButton("✓ Yᴇꜱ", callback_data="yes"),
              InlineKeyboardButton("✘ Nᴏ", callback_data="no")
              ]]

CANCEL_BUTTON = [[
                InlineKeyboardButton("☒ Cᴀɴᴄᴇʟ", callback_data="cancel")
                ]]

RTUSIKKSNNHBBBNNNZJJK = [[
                       ("Jᴏɪɴ Tᴇᴀᴍ"),
                       ("ツ Hɪʀᴇ Us")
                       ],[
                       ("Cʜᴀɴɴᴇʟs"),
                       ("Gʀᴏᴜᴘs")
                       ],[
                       ("Yᴏᴜᴛᴜʙᴇ"),
                       ("Aʙᴏᴜᴛ Us")
                       ],[
                       ("☏ Cᴏɴᴛᴀᴄᴛ Us")
                       ]]

GHEJISJSBSHWUS = """「 Aɪᴏᴍ Cᴏᴍᴘᴀɴʏ Hᴀs 2 Cʜᴀɴɴᴇʟs 」

〈 • @AIOM_BOTS

    • @AIOM_BOTS_UPDATES 〉"""

SGKGSFJFGFSTRDH = """「 Aɪᴏᴍ Cᴏᴍᴘᴀɴʏ Hᴀs 2 Gʀᴏᴜᴩꜱ 」

〈 • @AIOM_BOTS_GROUP

    • @ALLINONEMOVIESTALKS 〉"""

SFHODFHIK = "「 Sᴇɴᴅ Tʜᴇ Mᴇssᴀɢᴇ Tʜᴀᴛ Yᴏᴜ Wᴀɴᴛ Tᴏ Tᴇʟʟ Us 」"

JOINTETYSI = """<b>Tᴏ Jᴏɪɴ Oᴜʀ Tᴇᴀᴍ Yᴏᴜ Mᴜsᴛ Nᴇᴇᴅ To Cᴏᴍᴘʟᴇᴛᴇ Oᴜʀ Rᴇǫᴜɪʀᴇᴍᴇɴᴛs & Aɢʀᴇᴇ Tᴏ Tᴇʀᴍs</b>

```Dᴏ Yᴏᴜ Wᴀɴᴛ Tᴏ Cᴏɴᴛɪɴᴜᴇ?```"""

DGKKKKKK = """「 Aɪᴏᴍ Cᴏᴍᴘᴀɴʏ Hᴀs 1 Yᴏᴜᴛᴜʙᴇ Cʜᴀɴɴᴇʟ 」

〈 •https://youtube.com/channel/UCI152ovlGMZ_ekyJdcMFgXw  〉"""

JOINTBSJSI = [[
                InlineKeyboardButton("Cᴏɴᴛɪɴᴜᴇ ✓", callback_data="join")
                ]]

TRRYOBGYYUI = """∆ Yᴏᴜ Cᴀɴ Hɪʀᴇ Us Tᴏ

• Mᴀᴋᴇ Tᴇʟᴇɢʀᴀᴍ Bᴏᴛs

• Eᴅɪᴛ Tᴇʟᴇɢʀᴀᴍ Bᴏᴛs

• Mᴀᴋᴇ Wᴇʙsɪᴛᴇs (cᴏᴍɪɴɢ sᴏᴏɴ)

• Mᴀᴋᴇ Wʜᴀᴛsᴀᴘᴘ Bᴏᴛ (ᴄᴏᴍɪɴɢ sᴏᴏɴ)

Tʜᴇsᴇ Wᴏʀᴋs Aʀᴇ Cᴜʀʀᴇɴᴛʟʏ Fʀᴇᴇ"""

DFGUIJJHTT = [[
             InlineKeyboardButton("ϡ Hɪʀᴇ Us", callback_data="hire")
             ]]

GJDOSNDNXHDUSN = """Aɪᴏᴍ© Is A Oꜰꜰɪᴄɪᴀʟ Cᴏᴅɪɴɢ Rᴇʟᴇᴛᴇᴅ Cᴏᴍᴘᴀɴʏ 

Yᴏᴜ Cᴀɴ Jᴏɪɴ Oᴜʀ Tᴇᴀᴍ (ᴏʀ) Hɪʀᴇ Us Tᴏ Mᴀᴋᴇ Yᴏᴜ A Wᴏɴᴅᴇʀꜰᴜʟ Bᴏᴛ

Aɪᴏᴍ© Is Sᴛᴀʀᴛᴇᴅ Aᴛ 2020. Tʜᴇ Fɪʀsᴛ Pʀᴏᴊᴇᴄᴛ Oꜰ Aɪᴏᴍ Bᴏᴛ Is A Mᴏᴠɪᴇ Gʀᴏᴜᴘ Tʜᴇɴ A Bᴏᴛ Cʜᴀɴɴᴇʟ Aɴᴅ A Wᴇʙsɪᴛᴇ

Dᴏ Yᴏᴜ Nᴏᴡ Cᴏᴅɪɴɢ Jᴏɪɴ Us Wᴇ Cᴀɴ Mᴀᴋᴇ Lᴏᴛs Oꜰ Cᴏᴏʟ Sᴛᴜꜰꜰ Tᴏɢᴇᴛʜᴇʀ """

@ajvad.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    await message.reply(
        text=START_TEXT.format(message.from_user.mention),
        reply_markup=ReplyKeyboardMarkup(RTUSIKKSNNHBBBNNNZJJK, one_time_keyboard=True, resize_keyboard=True)
    )

@ajvad.on_message(filters.regex("Jᴏɪɴ Tᴇᴀᴍ") & filters.private)
async def my_handle16(bot, message):
    await message.reply(
        text=JOINTETYSI,
        reply_markup=InlineKeyboardMarkup(JOINTBSJSI)
    )

@ajvad.on_message(filters.regex("ツ Hɪʀᴇ Us") & filters.private)
async def my_handle6(bot, message):
    await message.reply(
        text=TRRYOBGYYUI,
        reply_markup=InlineKeyboardMarkup(DFGUIJJHTT),
        disable_web_page_preview=True
    )

@ajvad.on_message(filters.regex("Aʙᴏᴜᴛ Us") & filters.private)
async def my_havvndle6(bot, message):
    await message.reply(
        text=GJDOSNDNXHDUSN
    )

@ajvad.on_message(filters.regex("Cʜᴀɴɴᴇʟs") & filters.private)
async def my_havvndle6(bot, message):
    await message.reply(
        text=GHEJISJSBSHWUS
    )

@ajvad.on_message(filters.regex("Gʀᴏᴜᴘs") & filters.private)
async def my_havvccndle6(bot, message):
    await message.reply(
        text=SGKGSFJFGFSTRDH
    )

@ajvad.on_message(filters.regex("☏ Cᴏɴᴛᴀᴄᴛ Us") & filters.private)
async def my_hcndle6(bot, message):
    await message.reply(
        text=SFHODFHIK
    )

@ajvad.on_message(filters.regex("Yᴏᴜᴛᴜʙᴇ") & filters.private)
async def my_hcnle6(bot, message):
    await message.reply(
        text=DGKKKKKK
    )

@ajvad.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "join":
            await msg.message.edit(
                text="""Rᴇǫᴜɪʀᴇᴍᴇɴᴛs :

• Mᴜsᴛ Bᴇ A Kɴᴏᴡʟᴇᴅɢᴇ Iɴ Pʏᴛʜᴏɴ

• Eʟᴅᴇʀ Tʜᴀɴ 13 Yᴇᴀʀs

• Kɴᴏᴡʟᴇᴅɢᴇ Aʙᴏᴜᴛ Wᴇʙ Dᴇᴠᴇʟᴏᴘᴍᴇɴᴛ (ᴏᴘᴛɪᴏɴᴀʟ)

• Mᴜsᴛ Bᴇ Bᴏᴛ Dᴇᴠᴇʟᴏᴘᴇʀ Iɴ Tᴇʟᴇɢʀᴀᴍ

Σ Dᴏ Yᴏᴜ Wᴀɴᴛ Tᴏ Cᴏɴᴛɪɴᴜᴇ?""",
                reply_markup=InlineKeyboardMarkup(JOIN_BUTTON)
            
            )

    elif msg.data == "yes":
            await msg.message.edit(
                text="""Sᴇɴᴅ Mᴇ Tʜᴇsᴇ Dᴇᴛᴀɪʟs Tᴏ Jᴏɪɴ Oᴜʀ Tᴇᴀᴍ ☟

```• Fɪʀsᴛ Nᴀᴍᴇ :

• Lᴀsᴛ Nᴀᴍᴇ :

• Eᴍᴀɪʟ :

• Pʜᴏɴᴇ : (Oᴘᴛɪᴏɴᴀʟ)

• Aɢᴇ :

• Sᴋɪʟʟs :

• Oᴛʜᴇʀ :```""",
                reply_markup=InlineKeyboardMarkup(CANCEL_BUTTON)
            
            )

    elif msg.data == "cancel":
            await msg.message.edit(
                text="O"
            )
            await msg.message.edit(
                text="Oᴋ"
            )
            await msg.message.edit(
                text="Oᴋ T"
            )
            await msg.message.edit(
                text="Oᴋ Tʜ"
            )
            await msg.message.edit(
                text="Oᴋ Tʜᴇ"
            )
            await msg.message.edit(
                text="Oᴋ Tʜᴇɴ"
            )
            await msg.message.delete()
            await msg.message.reply(
                text=START_TEXT.format(msg.from_user.mention),
                reply_markup=InlineKeyboardMarkup(START_BUTTONS)
            )

    elif msg.data == "no":
            await msg.message.edit(
                text="O"
            )
            await msg.message.edit(
                text="Oᴋ"
            )
            await msg.message.edit(
                text="Oᴋ T"
            )
            await msg.message.edit(
                text="Oᴋ Tʜ"
            )
            await msg.message.edit(
                text="Oᴋ Tʜᴇ"
            )
            await msg.message.edit(
                text="Oᴋ Tʜᴇɴ"
            )
            await msg.message.delete()
            await msg.message.reply(
                text=START_TEXT.format(msg.from_user.mention),
                reply_markup=InlineKeyboardMarkup(START_BUTTONS)
            )

    elif msg.data == "hire":
            await msg.message.edit(
                text="""Wʜɪᴄʜ Bᴏᴛ Yᴏᴜ Wᴀɴᴛ Tᴏ Mᴀᴋᴇ/Eᴅɪᴛ

Aɴsᴡᴇʀ Tᴏ Dᴇᴠᴇʟᴏᴘᴇʀs Usɪɴɢ Tʜɪs Bᴏᴛ (ᴏʀ) Cᴏɴᴛᴀᴄᴛ [Aᴅᴍɪɴ](https://t.me/ajvadntr2)""",
                disable_web_page_preview=True
            )

ajvad.run()

