"""EMOJI 

.eye
.sry
.sml
.lol
.no
.dan

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "eye":

        await event.edit(input_str)

        animation_chars = [

            "👁👁\n  👄  =====> Aye Ja Na Gandu",
            "👁👁\n  👅  =====> Aye Ja Na Madarchod",    
            "👁👁\n  💋  =====> Aye Ja Na Randi",
            "👁👁\n  👄  =====> Aye Ja Na Betichod",
            "👁👁\n  👅  =====> Aye Ja Na Behenchod",
            " 👁👁\n 🍤  =====>Ab ja na lawde ke baal",
            "👁👁\n  💋  =====> Aye Ja Na Na Mard",
            "👁👁\n  👄  =====> Aye Ja Na Randi",
            "👁👁\n  👅  =====> Aye Ja Na Bhosdke",    
            "👁👁\n  💋  =====> Aye Ja Na Chutiye",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@borg.on(outgoing=True, pattern="^.repo$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Click [here](https://github.com/eonarmy/xuserbot) to open this lit af repo.")
			  
@borg.on(outgoing=True, pattern="^.sry$")
async def sorry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("😔Sorry😔")
	
@borg.on(outgoing=True, pattern="^.sml$")
async def smile(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("😄😄😄")			  
			 
@borg.on(outgoing=True, pattern="^.lol$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("😂😂😂")	
        
@borg.on(outgoing=True, pattern="^.no$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🙅‍♂️")    
        
@borg.on(outgoing=True, pattern="^.dan$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("😡")  
        
