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
          
          


#███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
#permissions
@client.event 
async def on_message(message):
        if message.content.upper().startswith("/WARN"):#sym
                    if message.author.id == "421664761483231232":
                          await client.send_message(message.channel, "The user has been warned")
                          args = message.content.split(" ")
                          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    
        if message.content.upper().startswith("/WARN"):#me
                    if message.author.id == "257324640160972801":
                          await client.send_message(message.channel, "The user has been warned")
                          args = message.content.split(" ")
                          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    
        if message.content.upper().startswith("/WARN"):#yuni
                    if message.author.id == "260255626691739649":
                          await client.send_message(message.channel, "The user has been warned")
                          args = message.content.split(" ")
                          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    
        if message.content.upper().startswith("/WARN"):#bxx
                    if message.author.id == "348682446159609856":
                          await client.send_message(message.channel, "The user has been warned")
                          args = message.content.split(" ")
                          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    
        if message.content.upper().startswith("/WARN"):#lemon
                    if message.author.id == "348442873747734528":
                          await client.send_message(message.channel, "The user has been warned")
                          args = message.content.split(" ")
                          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    
        if message.content.upper().startswith("/WARN"):#tender
                    if message.author.id == "443334562093858846":
                          await client.send_message(message.channel, "The user has been warned")
                          args = message.content.split(" ")
                          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    
        if message.content.upper().startswith("/WARN"):#chip
                    if message.author.id == "214006584286642176":
                          await client.send_message(message.channel, "The user has been warned")
                          args = message.content.split(" ")
                          await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
                    
#█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████        
#Trivia
        if message.content.upper().startswith("/TRIVIA"):
                    embed = discord.Embed(title="Trivia", description="Try some of these!", color=0)
                    embed.add_field(name="Category", value="These are trivia categories choose one category you like :)", inline=False)
                    embed.add_field(name="Games", value="Do /glevels", inline=True)
                    embed.add_field(name="Animals", value="Do /alevels", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
#CA
        if message.content.upper().startswith("/ALEVELS"):
                    embed = discord.Embed(title="Trivia", description="Game Levels", color=0)
                    embed.add_field(name="Levels", value="These are trivia level choose one level you like :)", inline=False)
                    embed.add_field(name="/aone", value="About biggest animal on Earth", inline=True)
                    embed.add_field(name="/atwo", value="About the fastest animal on Earth", inline=True)
                    embed.add_field(name="/athree", value="About the smallest animal on Earth", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/GRETURN"):
                    embed = discord.Embed(title="Trivia", description="Game Levels", color=0)
                    embed.add_field(name="Levels", value="These are trivia level choose one level you like :)", inline=False)
                    embed.add_field(name="/aone", value="About biggest animal on Earth", inline=True)
                    embed.add_field(name="/atwo", value="About the fastest animal on Earth", inline=True)
                    embed.add_field(name="/athree", value="About the smallest animal on Earth", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
#Animal 1
        if message.content.upper().startswith("/AONE"):
                    embed = discord.Embed(title="Trivia", description="Pick an answer by putting the command", color=0)
                    embed.add_field(name="Question", value="Whats the biggest animal on earth?", inline=False)
                    embed.add_field(name="Argentinosaurus", value="Do /1a1", inline=True)
                    embed.add_field(name="Blue whale", value="Do /1a2", inline=True)
                    embed.add_field(name="T rex", value="Do /1a3", inline=True)
                    embed.add_field(name="Spinosaurus", value="Do /1a4", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A1"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A2"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Correct! ~ Over 200 tons!", value="/greturn so you can play more and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A3"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A4"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/A1REVEAL"):
                    embed = discord.Embed(title="Trivia", description="Answer", color=0)
                    embed.add_field(name=":arrow_forward: The answer for animal 1 is the Blue Whale", value="Surprised? The Blue Whale is much heavier than any dinosaur", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
#Animal 2
        if message.content.upper().startswith("/ATWO"):
                    embed = discord.Embed(title="Trivia", description="Pick an answer by putting the command", color=0)
                    embed.add_field(name="Question", value="Whats the fastest animal on Earth?", inline=False)
                    embed.add_field(name="Cheetah", value="Do /1a1", inline=True)
                    embed.add_field(name="Peregrine Falcon", value="Do /1a2", inline=True)
                    embed.add_field(name="T rex", value="Do /1a3", inline=True)
                    embed.add_field(name="Spinosaurus", value="Do /1a4", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A1"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A2"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Correct! ~ Over 200 tons!", value="/greturn so you can play more and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A3"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1A4"):
                    embed = discord.Embed(title="Trivia", description="Animals", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/A1REVEAL"):
                    embed = discord.Embed(title="Trivia", description="Answer", color=0)
                    embed.add_field(name=":arrow_forward: The answer for animal 1 is the Blue Whale", value="Surprised? The Blue Whale is much heavier than any dinosaur", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
                                     
                                     
#CG
        if message.content.upper().startswith("/GLEVELS"):
                    embed = discord.Embed(title="Trivia", description="Game Levels", color=0)
                    embed.add_field(name="Levels", value="These are trivia level choose one level you like :)", inline=False)
                    embed.add_field(name="/gone", value="About the most downloaded game", inline=True)
                    embed.add_field(name="/gtwo", value="About the most money earning game", inline=True)
                    embed.add_field(name="/gthree", value="About the most popular game as of 2018", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/GRETURN"):
                    embed = discord.Embed(title="Trivia", description="Game Levels", color=0)
                    embed.add_field(name="Levels", value="These are trivia level choose one level you like :)", inline=False)
                    embed.add_field(name="/gone", value="About the most downloaded game", inline=True)
                    embed.add_field(name="/gtwo", value="About the most money earning game", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.add_field(name="Coming soon", value="...", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
#Game 1
        if message.content.upper().startswith("/GONE"):
                    embed = discord.Embed(title="Trivia", description="Pick an answer by putting the command", color=0)
                    embed.add_field(name="Question", value="What is the most downloaded game on iOS and android phones worldwide?", inline=False)
                    embed.add_field(name="Subway Surfers", value="Do /1g1", inline=True)
                    embed.add_field(name="Clash of clans", value="Do /1g2", inline=True)
                    embed.add_field(name="Candy Crush", value="Do /1g3", inline=True)
                    embed.add_field(name="Temple Run 2", value="Do /1g4", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1G1"):
                    embed = discord.Embed(title="Trivia", description="Games", color=7506394)
                    embed.add_field(name=":arrow_forward: Correct! ~ Over 1 Billion downloads", value="/greturn so you can play more and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1G2"):
                    embed = discord.Embed(title="Trivia", description="Games", color=7506394)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1G3"):
                    embed = discord.Embed(title="Trivia", description="Games", color=7506394)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/1G4"):
                    embed = discord.Embed(title="Trivia", description="Games", color=7506394)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g1reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/G1REVEAL"):
                    embed = discord.Embed(title="Trivia", description="Answer", color=7506394)
                    embed.add_field(name=":arrow_forward: The answer for game 1 is Subway Surfers", value="Over a billion players", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
#Game 2
        if message.content.upper().startswith("/GTWO"):
                    embed = discord.Embed(title="Trivia", description="Pick an answer by putting the command", color=0)
                    embed.add_field(name="Question", value="What is the most money earning game of all time?", inline=False)
                    embed.add_field(name="Fortnite", value="Do /2g1", inline=True)
                    embed.add_field(name="Pac-Man", value="Do /2g2", inline=True)
                    embed.add_field(name="Space Invaders", value="Do /2g3", inline=True)
                    embed.add_field(name="Crossfire", value="Do /2g4", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/2G1"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g2reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/2G2"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g2reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/2G3"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Correct! ~ Over 14 Billion dollars", value="/greturn so you can play more and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/2G4"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g2reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/G2REVEAL"):
                    embed = discord.Embed(title="Trivia", description="Answer", color=0)
                    embed.add_field(name=":arrow_forward: The answer for game 2 is Space Invaders", value="Over a 14 Billion dollars talk about money!", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
#Game 3
        if message.content.upper().startswith("/GTHREE"):
                    embed = discord.Embed(title="Trivia", description="Pick an answer by putting the command", color=0)
                    embed.add_field(name="Question", value="What is the most popular game as of 2018", inline=False)
                    embed.add_field(name="Fortnite", value="Do /3g1", inline=True)
                    embed.add_field(name="PUBG", value="Do /3g2", inline=True)
                    embed.add_field(name="Far Cry 5", value="Do /3g3", inline=True)
                    embed.add_field(name="Subnautica", value="Do /3g4", inline=True)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/3G1"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Correct! ~ Dude everybody was talking about it", value="/greturn so you can play more and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/3G2"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g2reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/3G3"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more and /trivia for the menu" , inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/3G4"):
                    embed = discord.Embed(title="Trivia", description="Games", color=0)
                    embed.add_field(name=":arrow_forward: Your answer is wrong", value="/greturn so you can play more or /g2reveal to reveal the answer and /trivia for the menu", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/G2REVEAL"):
                    embed = discord.Embed(title="Trivia", description="Answer", color=0)
                    embed.add_field(name=":arrow_forward: The answer for game 2 is Space Invaders", value="Over a 14 Billion dollars talk about money!", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)

          
     
#███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                    await client.send_message(message.channel, embed=embed)
#commands
            

        if message.content.upper().startswith("/SHIP"):
                    args = message.content.split(" ")
                    embed = discord.Embed(title="You shipped with", description="%s" % (" ".join(args[1:])), color=0)
                    await client.send_message(message.channel, embed=embed)
                    await client.send_message(message.channel, random.choice(["█ 10% Not compatible",                                   
                                                                             "██ 20% Somewhat compatible",
                                                                             "0% Haha thats fucking sad",
                                                                             "███ 30% Bad but atleast not the worst",
                                                                             "████ 40% Pretty average not bad ",
                                                                             "█████ 50% You have a good chance dude",
                                                                             "██████ 60% Above average, good",
                                                                             "███████ 70% This would work out, very good",
                                                                             "████████ 80% So close",
                                                                             "█████████ 90% Almost there!!",
                                                                             "██████████ 100% Perfect match"]))
        if message.content.upper().startswith('/AVATAR'):
                    await client.send_message(message.channel, "Heres your profile picture xS")
                    await client.send_message(message.channel, message.author.avatar_url)
        if message.content.upper().startswith('IM'):
                    await client.send_message(message.channel, "No you aren't you're depressed and lonely")
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
                    args = message.content.split(" ")
                    embed = discord.Embed(title="You shot :scream: :gun:", description="%s" % (" ".join(args[1:])), color=0)
                    await client.send_message(message.channel, embed=embed)  
        if message.content.upper().startswith("/BOTINV"):
                    embed = discord.Embed(title="Heres the invite :)", description="https://discordapp.com/oauth2/authorize?&client_id=438652352338198538&scope=bot&permissions=0", color=0x00ff00)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/RLINKS"):               
                    embed = discord.Embed(title="Enjoy :)", description="https://www.reddit.com/r/DiepioPartyLinks/new/", color=0)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/DASHBOARD"):
                    await client.send_message(message.channel, "http://schwiftybot.website2.me/")
        if message.content.upper().startswith("/VERSION"):
                    await client.send_message(message.channel, "The versions has been sent to you through DMs *Slides in*")
                    embed=discord.Embed(title="SchwiftyBot", url="http://schwiftybot.website2.me/", description="Note: The version command is relatively new so data before the command would not be processed", color=0)
                    embed.add_field(name="1.0.0", value="Added embedded /help text (5/7/18)", inline=False)
                    embed.add_field(name="1.1.0", value="Added version (5/8/18)", inline=False)
                    embed.add_field(name="1.1.1", value="Improved imbedded commands (5/8/18)", inline=False)
                    embed.add_field(name="1.2.1", value="Added /8ball command Usage = /8ball <question> (5/9/18)", inline=False)
                    embed.add_field(name="1.3.1", value="Improved embedded commands for /help (5/9/18)", inline=False)
                    embed.add_field(name="1.4.1", value="Removed /say because it could be used to ping everyone (5/9/18)", inline=False)
                    embed.add_field(name="1.5.1", value="Added a reposit for the bot /reposit (5/9/18)", inline=False)
                    embed.add_field(name="1.6.1", value="Made a coinflip command /coinflip (5/9/18)", inline=False)
                    embed.add_field(name="1.7.1", value="Added /info command (5/11/18)", inline=False)
                    embed.add_field(name="1.8.1", value="Added /avatar command (5/18/18)", inline=False)
                    embed.add_field(name="1.9.1", value="Added /warn command (Very WIP but still kinda works in my server and others)(5/18/18)", inline=False)
                    embed.add_field(name="1.9.2", value="Improved warn commands (5/18/18)", inline=False)
                    embed.add_field(name="2.0.2", value="Created a trivia command /trivia (5/20/18)", inline=False)
                    embed.add_field(name="2.1.2", value="Created a trivia command /trivia (5/20/18)", inline=False)
                    embed.add_field(name="2.1.3", value="Improved ship command and shoot(5/21/18)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.author, embed=embed)
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
                    embed = discord.Embed(title="Heres the website", description="http://www.teamfortress.com/", color=0)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/REPOSIT"):
                    await client.send_message(message.channel, "This is still in progress but its just a good look inside my bot")
                    await client.send_message(message.channel, "https://github.com/ItzSchwifty/ScwhiftyBot")
        if message.content.upper().startswith("/COINFLIP"):
                    userID = message.author.id 
                    await client.send_message(message.channel, random.choice(["<@%s> Its a heads!"  % (userID),
                                                                             "<@%s> Its a tails!" % (userID)]))
#████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████                    
#Sub commands
        if message.content.upper().startswith("//BOT"):
                    embed=discord.Embed(title="Hello! I'm Schwifty the Bot", url="http://schwiftybot.website2.me/", description = "I was created by a person named Schwifty#7692. This bot is under heavy development by only a single creator. The creator is also self taught and plans to spend absolutely no money at all. Anyways I created this bot mainly for fun at first but I instead put my time and effort into this. To support the bot and the creator, please go to our dashboard and send the invites to other servers, this will make me very happy and maybe feel a little bit succesful. Anyways have a good day everyone", color=0)
                    embed.set_footer(text='Support The Bot | SchwiftyBot')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("/INFO"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name="//bot", value="Shows the bot's information", inline=False)
                    embed.add_field(name="//<command>", value="Shows the purpose of the command and its usage. The two types are Ordinary which means no specific usage and the second one is Specific which means you have to use it in a specific way. Example //version", inline=False)                    
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//HELP"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It shows you all of the usable commands and excecutes the bot can do", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//BOTINV"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: The invite so this bot could join your own server. You could also give them this link. Both actions would support the bot", value="No specific usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//AVATAR"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives you your own avatar", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)            
        if message.content.upper().startswith("//VERSION"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives you the changelogs and updates of the bot", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//DASHBOARD"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives you the bot's dashboard or website check it out!", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//INFO"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives you more information about the commands and the bot", value="Usage = /info (bot or <command>) (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SUPPORT"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It makes an invite to the support server of the bot. Questions can be answered there", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//8BALL"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: It gives your magical answer or decision.", value="Usage = /8ball <question>  (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//COINFLIP"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Flips a coin heads or tails", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SHOOT"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Shoot someone!", value="Usage = /shoot <@user> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//PING"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Pong! >:)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//ID"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Gives you the ID of the person (Be in a voice chat first and say /summon)", value="Usage = /id <@user> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//PLAY"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Plays a music you desire (Be in a voice chat first and say /summon)", value="Usage = /play <song name> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//QUEUE"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Shows the queue of songs (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//PERMS"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Shows you your permissions (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SEARCH"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Searches a video on youtube then plays it on the vc (Be in a voice chat first and say /summon)", value="Usage = /search <video name> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SKIP"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Skips a song that is currently playing (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SUMMON"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Summons the bot into your VC (Be in a voice chat)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//CLEAN"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Cleans the entire queue (Be in a voice chat first and say /summon)", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//RLINKS"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Directly gives you the sandbox links to the subreddit of diep.io", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//TF2"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Gives you the announcements, updates and the website itself", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//WARN"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Warns a misbehaving member NOTE:Works only if you have an admin role", value="/warn <@member> <reason> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//SHIP"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Ship people and yourself", value="/ship <@user> (Specific)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
        if message.content.upper().startswith("//TRIVIA"):
                    embed=discord.Embed(title="Info Commands", description="This shows you other extended information and usages of the info commands", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Attaches a trivia file", value="No usage (Ordinary)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
                        
                        
                        
                        
                        
                        
                        
                        
        
                   
                    
                    
                    
                    
       
       



        if message.content.upper().startswith('/HELP'):
                    embed=discord.Embed(title="SchwiftyBot", url="http://schwiftybot.website2.me/", description="Schwifty the bot is a very early version of a bot. To help continue and support the bot go to our dashboard and invite it to your server! :cookie:", color=0)
                    embed.set_author(name="SchwiftyBot", url="http://schwiftybot.website2.me", icon_url="https://cdn.discordapp.com/attachments/323726246116589570/443672159064162314/Cabbage.jpg")
                    embed.add_field(name=":arrow_forward: Dashboard :cookie:", value="/help (Gives you the command lists)                                                                                                                                   /info (Gives you info about the bot and commands)                                                                                            /reposit (A good look inside the bot)                                                                                                                        /botinv (Invites the bot into your server)                                                                                           /version (Gives you the bot's version)                                                                                                              /dashboard (Gives you the bot's dashboard)                                                                                                                                  /support (Gives you to server's invite link for the owner's server)" , inline=False)
                    embed.add_field(name=":arrow_forward: Entertainment :video_game:", value="/8ball (Ohhh whats this?)                                                                                                       /trivia (Gives you questions to answer)                                                                                                                                                                                                         /avatar (Gives you your own profile picture)                                                                                                                    /coinflip (Flips a coin)                                                                                                                                                /ping (Pong!)                                                                                                                       /shoot <@user>(Shoot someone)                                                                                             /ship <@user> (Ship people and yourself cx)" , inline=False)
                    embed.add_field(name=":arrow_forward: Moderation :hotsprings:", value="/warn (Warns a member Only works if you have an admin role STILL WIP)", inline=False)
                    embed.add_field(name=":arrow_forward: Music :headphones:", value="/id <@user> <reason> (Gives your own ID)                                                                                       /play <song> (Plays the song)(Be in a voice chat first)                                                                       /queue (Gives the song list(s))                                                                                           /search (Enable you to search some stuff)                                                                                     /skip (Skips the song playing right now)                                                                                          /summon (Summons the bot) (CONNECT TO A VOICE CHANNEL)                                                                                               /clean (Cleans the entire queue)                                                                                                                                                   /perms (Shows you the permissions)", inline=False)
                    embed.add_field(name=":arrow_forward: Games :game_die:", value="/rlinks (Shows you the newest diep.io sanbox links)                                                                                                /tf2 (Gives you the website)", inline=False)
                    embed.set_footer(text='Support The Bot | SchwiftyBot ')
                    await client.send_message(message.channel, embed=embed)
                    os.system('cls' if os.name=='nt' else 'clear')

@client.event
async def on_reaction_remove(reaction, user):
     channel = reaction.message.channel
     await client.send_message(message.channel, "{} has removed {} from the message: {}".format(user.name, reaction.emoji, reaction.message.content))








          


          
               

                    







 

          
client.run("token")

