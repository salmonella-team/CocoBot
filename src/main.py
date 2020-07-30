from discord.ext import commands
import discord

import up
import dl
import settings

TOKEN = settings.TOKEN
BOT_HelloWorld = settings.BOT_HelloWorld

bot = commands.Bot(command_prefix="/koko ")

@bot.event
async def on_ready():
    print("Login OK!")
    await bot.get_channel(int(BOT_HelloWorld)).send("お～～～～はよ～～～ございま～～～～～～～～～す！！！")

@bot.command()
async def download(ctx, *args):
    url = args[0]
    title = dl.dlYoutube(url)
    file_name = title
    print(file_name)
    up.uploadFile(file_name)
    url = up.changeShareFile(file_name)
    await ctx.send(url)

bot.run(TOKEN)