import discord
from discord.ext import tasks, commands
import os
import io
import psutil
import random
from mcstatus import JavaServer
from colorama import Fore
import colorama, discord, motor, asyncio, os, motor.motor_asyncio, socket
import datetime
import requests
from importlib.metadata import version

bot = discord.Bot(intents=discord.Intents.all())

token = "put your bot's token here"  # bot token

bot.whitelist = [put user id here]


@bot.event
async def on_ready():
    print("logged in as Skynet",)
    presence.start()



#@tasks.loop()
#async def status_task() -> None:
#     await bot.change_presence(status=discord.Status.online, activity=discord.Game("with electicity⚡"))  #setting bot activities
#     await asyncio.sleep(60)

@tasks.loop(seconds=5)
async def presence():
    statements=[
      "on fire🔥",
      "at the speed of light🚀",
    ]
    await bot.change_presence(activity=discord.Game(name=f"{random.choice(statements)}"),status=discord.Status.online)


@bot.slash_command(description="Check bot's response latency")
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"Delay: {bot.latency} seconds", color=0xFFFFFF, timestamp=datetime.datetime.now())
    embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar)
    await ctx.respond(embed=embed)

@bot.slash_command(description="Stop the bot (only for admins)")
async def stop(ctx):
    if ctx.author.id in bot.whitelist:
        await ctx.respond("Stopping bot...")
        await bot.close()
    else:
        await ctx.respond("권한 부족!")

@bot.slash_command(description="Restart the bot (only for admins)")
async def restart(ctx):
    if ctx.author.id in bot.whitelist:
        await ctx.respond("restarting...", delete_after=1)
        os.system("screen -dmS bot.py python3 [put your bot's path here]")
        await bot.close()

    else:
        await ctx.respond("권한 부족!")

# purge message command
@bot.slash_command(description="Purge messages")
async def purge(ctx, amount: int):
    if ctx.author.id in bot.whitelist:
        await ctx.respond(f"Deleting {amount} messages...")
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send("채팅을 삭제하였습니다.", delete_after=3)
    else:
        await ctx.respond("권한 부족!")

@bot.slash_command(description="Send a message")
async def say(ctx, *, message):
    await ctx.respond(message)



# get server status command (cpu, ram, disk) 
@bot.slash_command(description="Get server status")
async def status(ctx):
    
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    embed = discord.Embed(title="Server Status", description="⚙️", color=0xFFFFFF,timestamp=datetime.datetime.now())
    embed.add_field(name="CPU", value=f"{cpu}%")
    embed.add_field(name="RAM", value=f"{ram}%")
    embed.add_field(name="DISK", value=f"{disk}%")
    embed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
    await ctx.respond(embed=embed)


# get minecraft server status command
@bot.slash_command(description="Get minecraft server status")
async def mcstatus(ctx, ip):
    server = JavaServer.lookup(ip)
    status = server.status()
    embed = discord.Embed(title="Minecraft Server Status", description="📊" , color=0xFFFFFF,timestamp = datetime.datetime.now())
    embed.add_field(name="Version", value=f"{status.version.name}") 
    embed.add_field(name="Players", value=f"{status.players.online}/{status.players.max}")
    embed.add_field(name="Description", value=f"{status.description}")
    time = datetime.datetime.now()
    embed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
    await ctx.respond(embed=embed)

# get bot invite link
@bot.slash_command(description="Get bot invite link")
async def invite(ctx):
    embed = discord.Embed(title="Invite Link", description="🔗", color=0xFFFFFF, timestamp=datetime.datetime.now())
    embed.add_field(name="Invite Link", value=f"[Click to invite to your server](put your bot invite link)")
    await ctx.respond(embed=embed)


bot.run(token)
