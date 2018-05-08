import discord
from discord.ext import commands
import asyncio
import time
from discord.voice_client import VoiceClient
import discord.ext.commands

startup_extensions = ["Music"]
Client = discord.Client ()
client = commands.Bot(command_prefix = "/")
bot = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
     await client.change_presence(game=discord.Game(name='/help | Support The Bot', type = 0))
     print("Bot is ready!")
     





class Main_Commands():
        def __init__(self, bot):
          self.bot = bot



@client.event 
async def on_message(message):
        if message.content.upper().startswith("/INVITE"):
                    await client.send_message(message.channel, "Heres the invite :) https://discord.gg/2ga7k6r")                    
        if message.content.upper().startswith("/PING"):
                    userID = message.author.id       
                    await client.send_message(message.channel, "<@%s> Pong! :ping_pong:" % (userID))
        if message.content.upper().startswith("/SAY"):
                    args = message.content.split(" ")
                    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        if message.content.upper().startswith("/SHOOT"):
                    await client.send_message(message.channel, "You shot :scream: :gun:")
                    args = message.content.split(" ")
                    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        if message.content.upper().startswith("/BOTINV"):
                    embed = discord.Embed(title="Heres the invite :)", description="https://discordapp.com/oauth2/authorize?&client_id=438652352338198538&scope=bot&permissions=0", color=0x00ff00)
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/RLINKS"):               
                    embed = discord.Embed(title="Enjoy :)", description="https://www.reddit.com/r/DiepioPartyLinks/new/", color=7506394)
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/DASHBOARD"):
                    await client.send_message(message.channel, "http://schwiftybot.website2.me/")



        if message.content.upper().startswith('/HELP'):
                    await client.send_message(message.channel, "**Awaiting Data...**")
                    embed = discord.Embed(title=":arrow_forward: Dashboard :cookie:", description="/help (Gives you the command lists)", color=0x00ff00)
                    embed.add_field(name="/botinv (Gives you the link where you can invite the bot into your server)", value="/dashboard (Gives you the bot's dashboard)", inline=False)
                    embed.add_field(name="/help (Gives you the command lists)", value="/invite (Gives you to server's invite link for the owner's server", inline=False)
                    embed.add_field(name=":arrow_forward: Entertainment :video_game:", value="/shoot <@user>(Shoot someone)", inline=False)
                    embed.add_field(name="/ping (Pong!)", value="/say <text>(Say something)", inline=False)
                    embed.add_field(name=":arrow_forward: Moderation :hotsprings:", value="Coming soon", inline=False)
                    embed.add_field(name=":arrow_forward: Music :headphones:", value="/id <@user> (Gives your own ID)", inline=False)
                    embed.add_field(name="/play <song> (Plays the song)` (**Be in a voice chat first**)", value="/queue (Gives the song list(s))", inline=False)
                    embed.add_field(name="/search (Enable you to search some stuff)", value="/skip (Skips the song playing right now)", inline=False)
                    embed.add_field(name="/summon (Summons the bot)` (**SAY THIS WHEN YOU CONNECT TO A VOICE CHANNEL**)", value="/clean (Cleans the entire queue)", inline=False)
                    embed.add_field(name="/perms (Shows you the permissions)", value="ً", inline=False)
                    embed.add_field(name=":arrow_forward: `Games` :game_die:", value="/rlinks (Shows you the newest diep.io sanbox links)", inline=False)
                    await client.send_message(message.channel, embed=embed)








client.login(process.env.NDM4NjUyMzUyMzM4MTk4NTM4.DdKfGg.SipN9fy6vjBXq7bbsKtnXvsnEpw);
          
client.run("NDM4NjUyMzUyMzM4MTk4NTM4.DcHw8g.biB7ZgXREEZt3M-Ccg4MYf9CHmU")

