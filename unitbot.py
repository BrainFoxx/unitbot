from telethon import TelegramClient
from telethon.sync import events
import time
import random

api_id = 0123456 # change to your api id
api_hash = "2gjtpwn65kwlfbskwq2kb" # change to your api hash


idd = 0

with TelegramClient("foxx", api_id, api_hash) as client:
    get_mine = client.get_me()

    @client.on(events.NewMessage(pattern=";chats", outgoing=True))
    async def chatss(event):
        liist = []
        async for dialog in client.iter_dialogs():
            gg = f"{dialog.name} : {dialog.id}"
            liist.append(gg)
        await event.delete()
        await event.respond("Все твои чаты: ")
        await event.respond(str(liist))
        print(idd)

    @client.on(events.NewMessage(pattern=";repeater (\w+)", outgoing=True))
    async def set_id(event):
        # await event.respond('ЧТобы узнать все id пиши ;chats')
        global idd
        idd = event.pattern_match.group(1)
        await event.edit(f"Ты выбрал {idd}")
        # await event.respond(f'Ты выбрал {idd}')

    @client.on(events.NewMessage(func=lambda e: e.is_private, incoming=True))
    async def repeater(event):
        user_from = await event.client.get_entity(event.from_id)
        if int(idd) == user_from.id:
            await event.respond("Ты в игноре")
        else:
            pass

    @client.on(events.NewMessage(pattern=";spam(?: |$)(.*)", outgoing=True))
    async def spam(event):
        await event.delete()
        get_text = event.text[6:]
        ldr = get_text.split(" ", 1)
        counter = int(ldr[0])
        mesg = ldr[1]
        for i in range(counter):
            await event.respond(mesg)

    @client.on(events.NewMessage(pattern=";ran (\w+)", outgoing=True))
    async def randomer(event):
        get_count = int(event.pattern_match.group(1))
        randomizee = random.randint(0, get_count)
        await event.edit(str(randomizee))

    @client.on(events.ChatAction())
    async def joiiner(event):
        if event.user_joined:
            await event.respond(f'{event.user.first_name}, чей Крым?')

    """
    @client.on(events.NewMessage(pattern=";mag(?: |$)(.*)", outgoing=True))
    async def magic(event):
        await event.delete()
        get_text = event.text[5:]

        for i in get_text:
            await event.respond(i)
    """


    @client.on(events.NewMessage(pattern=";mag(?: |$)(.*)", outgoing=True))
    async def magic(event):
        get_text = event.text[5:]
        dict = ''
        for i in get_text:
            if i == ' ':
                dict += '.'
            await event.edit(f"{dict}{i}")
            dict = dict + i
            time.sleep(0.553)
    client.run_until_disconnected()
