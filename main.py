"""
Parabois bot
"""

from os import getenv
from dotenv import load_dotenv
import discord
from keep_bot_alive import keep_alive

load_dotenv()
token = getenv("TOKEN")
if not token:
    raise NameError("Token env variable is not defined")


client = discord.Client()

@client.event
async def on_ready():
    """Login handler"""
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    """Message handler"""
    if message.author == client.user:
        return
    if message.content.startswith("+test"):
        await message.channel.send("I am alive!")

keep_alive()
client.run(token)
