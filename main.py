import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

#-----SETUP-----#

prefix = "-"

#use the .env feature to hide your token

keep_alive()
token = (os.environ['TOKEN'])

#---------------#

bot = commands.Bot(command_prefix=prefix,
 help_command=None,
 case_insensitive=True,
  self_bot=True)
@bot.event
async def on_ready():
    activity = discord.Game(name="Auto Owo enabled", type=4)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    
print('''THANKS FOR USING THIS sall SELF BOT IS READY USE -help TO KNOW ALL COMMANDS 

Sall selfbot is ready!
''')
@bot.command()
async def help(ctx):
  await ctx.send('```created by devrock / cinderace make sure to join my server```Here is My command :- **-autoOwO**,**-stopautoOwO**,**-Owobanbypass** thats it. ```banner.txt , etc<333```https://imgur.com/a/S21UaJ7 , ')

@bot.command(pass_context=True)
async def autoOwO(ctx):
    await ctx.message.delete()
    await ctx.send('auto OwO  is now **enabled**!')
    global dmcs
    dmcs = True
    while dmcs:
        async with ctx.typing():
            await asyncio.sleep(5)
          await ctx.send('owoh')
           print(f"                              {Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo flip 500')
          print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo flip 500')
          print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo flip 500')
          print(f"{Fore.GREEN}succefully owoh")
            await asyncio.sleep(15)
            await ctx.send('owo flip 500')