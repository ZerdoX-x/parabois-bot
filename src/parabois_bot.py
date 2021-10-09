"""
Parabois bot
"""

from os import getenv

import discord
import youtube_dl
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TOKEN")
PREFIX = getenv("PREFIX")
if not TOKEN:
    raise NameError("Token env variable is not defined")

client = commands.Bot(command_prefix=PREFIX or "..")


@client.event
async def on_ready():
    """Login handler"""
    print(f"Logged in as {client.user}")


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
        url = info["formats"][0]["url"]
        source = await discord.FFmpegOpusAudio.from_probe(
            url, **FFMPEG_OPTIONS
        )
        try:
            if not ctx.voice_client.is_connected():
                pass
        except AttributeError:
            channel = ctx.author.voice.channel
            await channel.connect()

        ctx.voice_client.play(source)


@client.command()
async def leave(ctx):
    """Leave voice channel"""
    server = ctx.message.guild.voice_client
    await server.disconnect()


@client.command()
async def pause(ctx):
    """Pause current track"""
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send("Paused :pause_button:")
    else:
        await ctx.send("No playing audio, at the moment")


@client.command()
async def resume(ctx):
    """Resume current track"""
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send("Resume :arrow_forward:")
    else:
        await ctx.send("No song paused, at the moment")


def main():
    """Start bot"""
    client.run(TOKEN)


main()
