from telethon import TelegramClient, events, sync
from telethon import functions, types
import asyncio

api_id = xxxxxx
api_hash = ''

loop = asyncio.get_event_loop() 

client = TelegramClient('session_name', api_id, api_hash, loop=loop) 
client.start()

@client.on(events.NewMessage())
async def my_event_handler(event):
    print(event.peer_id)
    print(event.text)
    #await event.respond('Hey!')
   
async def main():
    while True:
        
        await asyncio.sleep(1)

client.loop.run_until_complete(main())