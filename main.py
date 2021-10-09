"""
Parabois bot
"""

from os import getenv
from dotenv import load_dotenv
import discord

load_dotenv()
token = getenv("TOKEN")
print(token)

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

client.run(token)
