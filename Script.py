class script(object):
    START_TXT = """đ·đŽđ»đŸ {},
đŒđ đœđ°đŒđŽ đžđ <a href=https://t.me/{}>{}</a> I am a powerful autofilter bot with some more featues.. âĄđ«đ«đ«"""
    HELP_TXT = """đ·đŽđ {}
đ·đŽđđŽ đžđ đđ·đŽ đ·đŽđ»đż đ”đŸđ đŒđ đČđŸđŒđŒđ°đœđłđ."""
    ABOUT_TXT = """âź đŒđ đœđ°đŒđŽ: {}
âź đČđđŽđ°đđŸđ: <a href=https://t.me/metrohdmovies>đđđđđđđđ</a>
âź đ»đžđ±đđ°đđ: đżđđđŸđ¶đđ°đŒ
âź đ»đ°đœđ¶đđ°đ¶đŽ: đżđđđ·đŸđœ đč
âź đłđ°đđ° đ±đ°đđŽ: đŒđŸđœđ¶đŸ đłđ±
âź đ±đŸđ đđŽđđđŽđ: RENDER
âź đ±đđžđ»đł đđđ°đđđ: v1.0.2 [ đ±đŽđđ° ]
âź Test creator â€ïžâ€ïžđ€"""

    PRIVATEBOT_TXT = """<b>đżđđžđđ°đđŽ đ±đŸđ đ”đŸđ đđŸđ</b>
<b>âșâș đłđŸ đđŸđ đđ°đœđ đ° đ±đŸđ đđ°đŒđŽ đ»đžđșđŽ đđ·đžđ</b>
<b>âșâș đđžđđ· đ°đ»đ» đđŸđđ đČđđŽđłđžđđ</b>
<b>âșâș đđžđđ· đđŸđđ đŸđđœđŽđđđ·đžđż</b>
<b>âșâș đČđŸđœđđ°đČđ đŒđŽ <a href=https://t.me/Metrorequestbot>đđđđđđđđ</a></b>"""

    SOURCE_TXT = """<b>Donation</b>

âȘŒ <b>đđšđź đđđ§ đđšđ§đđ­đ đđ§đČ đđŠđšđźđ§đ­ đđšđź đđđŻđ đł. 

<b>âââââââââá Payment Methods áâââââââââ

âź đđŒđŒđŽđčđČđŁđźđ
âź đŁđźđđđș
âź đŁđ”đŒđ»đČđŁđČ
âź đŁđźđđŁđźđč

_đđšđ§đ­đđđ­ đđ đđšđ« đđ§đšđ° đđđšđźđ­ đđĄđ đđđČđŠđđ§đ­ đđ§đđš_
ââââââââââââá <a href=https://t.me/Metrorequestbot><b>đđđ­đ«đš đđąđ„đ­đđ« đđšđ­</b></a> áââââââââââââ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and á©áá©á­ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. đđđ­đ«đš đđąđ„đ­đđ« đđšđ­ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âŸ /filter - <code>add a filter in chat</code>
âŸ /filters - <code>list all the filters of a chat</code>
âŸ /del - <code>delete a specific filter in chat</code>
âŸ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- đđđ­đ«đš đđąđ„đ­đđ« đđšđ­ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. đđđ­đ«đš đđąđ„đ­đđ« đđšđ­ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/metrohdmovies)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âŸ /connect  - <code>connect a particular chat to your PM</code>
âŸ /disconnect  - <code>disconnect from a chat</code>
âŸ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of đđđ­đ«đš đđąđ„đ­đđ« đđšđ­

<b>Commands and Usage:</b>
âŸ /id - <code>get id of a specifed user.</code>
âŸ /info  - <code>get information about a user.</code>
âŸ /imdb  - <code>get the film information from IMDb source.</code>
âŸ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my đđđđđâĄ

<b>Commands and Usage:</b>
âŸ /logs - <code>to get the rescent errors</code>
âŸ /stats - <code>to get status of files in db.</code>
âŸ /delete - <code>to delete a specific file from db.</code>
âŸ /users - <code>to get list of my users and ids.</code>
âŸ /chats - <code>to get list of the my chats and ids </code>
âŸ /leave  - <code>to leave from a chat.</code>
âŸ /disable  -  <code>do disable a chat.</code>
âŸ /ban  - <code>to ban a user.</code>
âŸ /unban  - <code>to unban a user.</code>
âŸ /channel - <code>to get list of total connected channels</code>
âŸ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """âź đđŸđđ°đ» đ”đžđ»đŽđ: <code>{}</code>
âź đđŸđđ°đ» đđđŽđđ: <code>{}</code>
âź đđŸđđ°đ» đČđ·đ°đđ: <code>{}</code>
âź đđđŽđł đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±
âź đ”đđŽđŽ đđđŸđđ°đ¶đŽ: <code>{}</code> đŒđđ±"""
    LOG_TEXT_G = """#đđđ°đđ«đšđźđ©
âź đđ«đšđźđ© âșâș {}(<code>{}</code>)
âź đđšđ­đđ„ đđđŠđđđ«đŹ âșâș <code>{}</code>
âź đđđđđ đđČ âșâș {}
"""
    LOG_TEXT_P = """#đđđ°đđŹđđ«
âź đđ âșâș <code>{}</code>
âź đđđŠđ âșâș {}
"""
    CARBON_TXT = """ <b>đČđ°đđ±đŸđœ đŒđŸđłđđ»đŽ</b>

<b>đđŸđ đČđ°đœ đ±đŽđ°đđđžđ”đ đđŸđđ đČđŸđłđŽđ đ±đ đđđžđœđ¶ đđ·đ đ”đŽđ°đđđđŽ...</b>

<b>đČđŸđŒđŒđ°đœđł.!</b>
<b>/carbon âșâș đđŽđżđ»đ đđŸ đ°đœđ đđŽđđ đŒđŽđđđ°đ¶đŽ</b>

<b>đđŸđđșđ đŸđœ đ±đŸđđ· đ¶đđŸđđż đ°đœđł đżđŒ</b>
<b>đČđđŽđłđžđđ âșâș</b> <a href=https://t.me/metrohdmovies>ĐŒŃŃŃÏ</a></b>"""
