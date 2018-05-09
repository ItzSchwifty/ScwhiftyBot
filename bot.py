#███                       ███ █████████  ██         █████████     █████████     ████          ████ █████████
# ███                     ███  ██         ██       ████      ██  ████      ████  ██ ██        ██ ██ ██
#  ███                   ███   ██         ██       ██            ██          ██  ██  ██      ██  ██ ██
#   ███      ██████     ███    █████████  ██       ██            ██          ██  ██   ██    ██   ██ █████████
#    ███    ███  ███   ███     ██         ██       ██            ██          ██  ██    ██  ██    ██ ██
#     ███ ███     ███ ███      ██         ██       ████      ██  ████      ████  ██     ████     ██ ██
#      ████         ████       █████████  ████████   █████████     ██████████    ██              ██ █████████


import discord
from discord.ext import commands
import asyncio
import time
from discord.voice_client import VoiceClient
import discord.ext.commands
import random
from discord.ext.commands import Bot
import os
import re

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
        if message.content.upper().startswith("/SUPPORT"):
                    await client.send_message(message.channel, "Heres the server :) https://discord.gg/2ga7k6r")                    
        if message.content.upper().startswith("/PING"):
                    userID = message.author.id       
                    await client.send_message(message.channel, "<@%s> Pong! :ping_pong:" % (userID))
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
        if message.content.upper().startswith("/VERSION"):
                    await client.send_message(message.channel, "**The version command is relatively new so data before the command would not be processed**")
                    embed = discord.Embed(title="1.0.0", description="Added embedded /help text (5/7/18)", color=0x00ff00)
                    embed.add_field(name="1.1.0", value="Added version (5/8/18)", inline=False)
                    embed.add_field(name="1.1.1", value="Improved imbedded commands (5/8/18)", inline=False)
                    embed.add_field(name="1.2.1", value="Added /8ball command Usage = /8ball <question> (5/9/18)", inline=False)
                    embed.add_field(name="1.3.0", value="Improved embedded commands for /help (5/9/18)", inline=False)
                    embed.add_field(name="1.4.0", value="Removed /say because it could be used to ping everyone (5/9/18)", inline=False)
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/8BALL"):
                    args = message.content.split(" ")
                    await client.send_message(message.channel, random.choice(["It is certain :8ball:",                                   
                                                                             "It is decidedly so :8ball:",
                                                                             "Without a doubt :8ball:",
                                                                             "Yes, definitely :8ball:",
                                                                             "You may rely on it :8ball:",
                                                                             "As I see it, yes :8ball:",
                                                                             "Most likely :8ball:",
                                                                             "Outlook good :8ball:",
                                                                             "Yes :8ball:",
                                                                             "Signs point to yes :8ball:",
                                                                             "Reply hazy try again :8ball:",
                                                                             "Ask again later :8ball:",
                                                                             "Better not tell you now :8ball:",
                                                                             "Cannot predict now :8ball:",
                                                                             "Concentrate and ask again :8ball:",
                                                                             "Don't count on it :8ball:",
                                                                             "My reply is no :8ball:",
                                                                             "My sources say no :8ball:",
                                                                             "Outlook not so good :8ball:",
                                                                             "Very doubtful :8ball:"]))
        
                   
                    
                    
                    
                    
       
       



        if message.content.upper().startswith('/HELP'):
                    embed=discord.Embed(title="SchwiftyBot", url="http://schwiftybot.website2.me/", description="Schwifty the bot is a very early version of a bot. To help continue and support the bot go to our dashboard and invite it to your server! :cookie:", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443674649608585216/tw.png")
                    embed.add_field(name=":arrow_forward: Dashboard :cookie:", value="/help (Gives you the command lists)                                                                               /botinv (Invites the bot into your server)                                                                                           /version (Gives you the bot's version)                                                                                                              /dashboard (Gives you the bot's dashboard)                                                                                                                                  /support (Gives you to server's invite link for the owner's server)" , inline=False)
                    embed.add_field(name=":arrow_forward: Entertainment :video_game:", value="/8ball (Ohhh whats this?)                                                                                                                                                      /ping (Pong!)                                                                                                                                           /say <text>(Say something)                                                                                                                                        /shoot <@user>(Shoot someone)" , inline=False)
                    embed.add_field(name=":arrow_forward: Moderation :hotsprings:", value="Coming soon", inline=False)
                    embed.add_field(name=":arrow_forward: Music :headphones:", value="/id <@user> (Gives your own ID)                                                                                       /play <song> (Plays the song)(Be in a voice chat first)                                                                       /queue (Gives the song list(s))                                                                                           /search (Enable you to search some stuff)                                                                                     /skip (Skips the song playing right now)                                                                                          /summon (Summons the bot) (CONNECT TO A VOICE CHANNEL)                                                                                               /clean (Cleans the entire queue)                                                                                                                                                   /perms (Shows you the permissions)", inline=False)
                    embed.add_field(name=":arrow_forward: `Games` :game_die:", value="/rlinks (Shows you the newest diep.io sanbox links)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
                    os.system('cls' if os.name=='nt' else 'clear')








          


          
               

                    







 

          
client.run("[token]")

