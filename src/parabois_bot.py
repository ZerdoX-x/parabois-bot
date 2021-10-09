"""
Parabois bot
"""

from os import getenv

import discord
import youtube_dl
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = getenv("TOKEN")
PREFIX = getenv("PREFIX")
if not TOKEN:
    raise NameError("Token env variable is not defined")

client = commands.Bot(command_prefix=PREFIX or '..')


@client.event
async def on_ready():
    """Login handler"""
    print(f"Logged in as {client.user}")


@client.command()
async def join(ctx):
    """Join voice channel"""
    channel = ctx.author.voice.channel
    await channel.connect()


FFMPEG_OPTIONS = {
    "before_options": """
        -reconnect 1
        -reconnect_streamed 1
        -reconnect_delay_max 5
    """,
    "options": "-vn",
}
YDL_OPTIONS = {
    "format": "bestaudio",
}


@client.command()
async def play(ctx, url):
    """Play yt video by link"""
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url = info['formats'][0]['url']
        source = \
            await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
        ctx.voice_client.play(source)


@client.command()
async def leave(ctx):
    """Leave voice channel"""
    server = ctx.message.guild.voice_client
    await server.disconnect()


def main():
    """Start bot"""
    client.run(TOKEN)


main()
