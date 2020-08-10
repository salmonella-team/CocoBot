from discord.ext import commands
import discord

import up
import dl
import settings
import size

TOKEN = settings.TOKEN
BOT_HelloWorld = settings.BOT_HelloWorld

bot = commands.Bot(command_prefix="/coco ")

@bot.event
async def on_ready():
    print("Login OK!")

@bot.command()
async def download(ctx, *args):
    if len(args) >= 2:
        await ctx.send("引数が不正")
        return
    await ctx.send("ダウンロード開始")
    url = args[0]
    title = dl.dlYoutube(url)
    file_name = title
    await ctx.send("まもなくファイルがアップロードされます")
    file_size = size.fetch_file_size(file_name)
    if file_size > 400000000:
        await ctx.send("ファイルサイズが大きすぎます")
        return
    up.uploadFile(file_name)
    url = up.changeShareFile(file_name)
    await ctx.send(url)

bot.run(TOKEN)