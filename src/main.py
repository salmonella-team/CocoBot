from discord.ext import commands
import discord

import up
import dl
import settings

TOKEN = settings.TOKEN
BOT_HelloWorld = settings.BOT_HelloWorld

bot = commands.Bot(command_prefix="/coco ")

@bot.event
async def on_ready():
    print("Login OK!")
    await bot.get_channel(int(BOT_HelloWorld)).send("お～～～～はよ～～～ございま～～～～～～～～～す！！！")

@bot.command()
async def download(ctx, *args):
    await ctx.send("ダウンロード開始")
    url = args[0]
    title = dl.dlYoutube(url)
    print(title)
    file_name = title
    print(file_name)
    await ctx.send("まもなくファイルがアップロードされます")
    up.uploadFile(file_name)
    url = up.changeShareFile(file_name)
    await ctx.send(url)

bot.run(TOKEN)