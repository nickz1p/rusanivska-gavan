import asyncio
from pyrogram import Client

api_id = 9963453

api_hash = "3cff28aa68fe29ef514cd004bf50c1ea"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())