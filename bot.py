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
        if message.content.upper().startswith("/SUMMON"):
                    await client.send_message(message.channel, "Dont put two bots in the same VC please. Beep Boop")
        if message.content.upper().startswith("/SUPPORT"):
                    await client.send_message(message.channel, "Heres the server :) https://discord.gg/2ga7k6r")
        if message.content.upper().startswith("/PLAY"):
                    await client.send_message(message.channel, "**Awaiting Data...**")  
        if message.content.upper().startswith("/PING"):
                    userID = message.author.id       
                    await client.send_message(message.channel, "<@%s> Pong! :ping_pong:" % (userID))
        if message.content.upper().startswith("/SHOOT"):
                    await client.send_message(message.channel, "You shot :scream: :gun:")
                    args = message.content.split(" ")
                    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        if message.content.upper().startswith("/BOTINV"):
                    embed = discord.Embed(title="Heres the invite :)", description="https://discordapp.com/oauth2/authorize?&client_id=438652352338198538&scope=bot&permissions=0", color=0x00ff00)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/RLINKS"):               
                    embed = discord.Embed(title="Enjoy :)", description="https://www.reddit.com/r/DiepioPartyLinks/new/", color=7506394)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/DASHBOARD"):
                    await client.send_message(message.channel, "http://schwiftybot.website2.me/")
        if message.content.upper().startswith("/VERSION"):
                    embed=discord.Embed(title="SchwiftyBot", url="http://schwiftybot.website2.me/", description="Note: The version command is relatively new so data before the command would not be processed", color=0x1b9aa0)
                    embed.add_field(name="1.0.0", value="Added embedded /help text (5/7/18)", inline=False)
                    embed.add_field(name="1.1.0", value="Added version (5/8/18)", inline=False)
                    embed.add_field(name="1.1.1", value="Improved imbedded commands (5/8/18)", inline=False)
                    embed.add_field(name="1.2.1", value="Added /8ball command Usage = /8ball <question> (5/9/18)", inline=False)
                    embed.add_field(name="1.3.0", value="Improved embedded commands for /help (5/9/18)", inline=False)
                    embed.add_field(name="1.4.0", value="Removed /say because it could be used to ping everyone (5/9/18)", inline=False)
                    embed.add_field(name="1.5.0", value="Added a reposit for the bot /reposit (5/9/18)", inline=False)
                    embed.add_field(name="1.6.0", value="Made a coinflip command /coinflip (5/9/18)", inline=False)
                    embed.add_field(name="1.7.0", value="Added /info command (5/11/18)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
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
        if message.content.upper().startswith("/TF2"):               
                    embed = discord.Embed(title="Heres the website", description="http://www.teamfortress.com/", color=7506394)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/REPOSIT"):
                    await client.send_message(message.channel, "This is still in progress but its just a good look inside my bot")
                    await client.send_message(message.channel, "https://github.com/ItzSchwifty/ScwhiftyBot")
        if message.content.upper().startswith("/COINFLIP"):
                    userID = message.author.id 
                    await client.send_message(message.channel, random.choice(["<@%s> Its a heads!"  % (userID),
                                                                             "<@%s> Its a tails!" % (userID)]))
        if message.content.upper().startswith("//BOT"):
                    embed=discord.Embed(title="Hello! I'm Schwifty the Bot", url="http://schwiftybot.website2.me/", description = "I was created by a person named Schwifty#7692. This bot is under heavy development by only a single creator. The creator is also self taught and plans to spend absolutely no money at all. Anyways I created this bot mainly for fun at first but I instead put my time and effort into this. To support the bot and the creator, please go to our dashboard and send the invites to other servers, this will make me very happy and maybe feel a little bit succesful. Anyways have a good day everyone", color=0x1b9aa0)
                    embed.set_footer(text='Support The Bot | SchwiftyBot')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/INFO"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name="//bot", value="Shows the bot's information", inline=False)
                    embed.add_field(name="//<command>", value="Shows the purpose of the command and its usage. The two types are Ordinary which means no specific usage and the second one is Specific which means you have to use it in a specific way. Example //version", inline=False)                    
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//HELP"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It shows you all of the usable commands and excecutes the bot can do", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//BOTINV"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: The invite so this bot could join your own server. You could also give them this link. Both actions would support the bot", value="No specific usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//VERSION"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives you the changelogs and updates of the bot", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//DASHBOARD"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives you the bot's dashboard or website check it out!", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//INFO"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives you more information about the commands and the bot", value="Usage = /info (bot or <command>) (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SUPPORT"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It makes an invite to the support server of the bot. Questions can be answered there", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//8BALL"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives your magical answer or decision.", value="Usage = /8ball <question>  (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//COINFLIP"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Flips a coin heads or tails", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SHOOT"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Shoot someone!", value="Usage = /shoot <@user> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//PING"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Pong! >:)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//ID"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Gives you the ID of the person (Be in a voice chat first and say /summon)", value="Usage = /id <@user> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//PLAY"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Plays a music you desire (Be in a voice chat first and say /summon)", value="Usage = /play <song name> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//QUEUE"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Shows the queue of songs (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//PERMS"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Shows you your permissions (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SEARCH"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Searches a video on youtube then plays it on the vc (Be in a voice chat first and say /summon)", value="Usage = /search <video name> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SKIP"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Skips a song that is currently playing (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SUMMON"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Summons the bot into your VC (Be in a voice chat)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//CLEAN"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Cleans the entire queue (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//RLINKS"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Directly gives you the sandbox links to the subreddit of diep.io", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//TF2"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Gives you the announcements, updates and the website itself", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
                        
                        
                        
                        
                        
                        
                        
                        
        
                   
                    
                    
                    
                    
       
       



        if message.content.upper().startswith('/HELP'):
                    embed=discord.Embed(title="SchwiftyBot", url="http://schwiftybot.website2.me/", description="Schwifty the bot is a very early version of a bot. To help continue and support the bot go to our dashboard and invite it to your server! :cookie:", color=0x1b9aa0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Dashboard :cookie:", value="/help (Gives you the command lists)                                                                                                                                   /info (Gives you info about the bot and commands)                                                                                            /reposit (A good look inside the bot)                                                                                                                        /botinv (Invites the bot into your server)                                                                                           /version (Gives you the bot's version)                                                                                                              /dashboard (Gives you the bot's dashboard)                                                                                                                                  /support (Gives you to server's invite link for the owner's server)" , inline=False)
                    embed.add_field(name=":arrow_forward: Entertainment :video_game:", value="/8ball (Ohhh whats this?)                                                                                                                          /coinflip (Flips a coin)                                                                                                                                                /ping (Pong!)                                                                                                                                                                                                                                                                                   /shoot <@user>(Shoot someone)" , inline=False)
                    embed.add_field(name=":arrow_forward: Moderation :hotsprings:", value="Coming soon", inline=False)
                    embed.add_field(name=":arrow_forward: Music :headphones:", value="/id <@user> (Gives your own ID)                                                                                       /play <song> (Plays the song)(Be in a voice chat first)                                                                       /queue (Gives the song list(s))                                                                                           /search (Enable you to search some stuff)                                                                                     /skip (Skips the song playing right now)                                                                                          /summon (Summons the bot) (CONNECT TO A VOICE CHANNEL)                                                                                               /clean (Cleans the entire queue)                                                                                                                                                   /perms (Shows you the permissions)", inline=False)
                    embed.add_field(name=":arrow_forward: Games :game_die:", value="/rlinks (Shows you the newest diep.io sanbox links)                                                                                                /tf2 (Gives you the website)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
                    os.system('cls' if os.name=='nt' else 'clear')








          


          
               

                    







 

          
client.run("token")

