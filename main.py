"""
Parabois bot
"""
from os import getenv
from dotenv import load_dotenv
import discord, youtube_dl
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

load_dotenv()
token = getenv("TOKEN")
if not token:
    raise NameError("Token env variable is not defined")

@client.event
async def on_ready():
    """Login handler"""
    print(f"Logged in as {client.user}")

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def play(ctx, url):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':'bestaudio'}

    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)

@client.command()
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

def app():
    """Start bot"""
    client.run(token)

app()
