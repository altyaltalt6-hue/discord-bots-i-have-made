import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix= '!',intents=intents)

#put the names of your mp3 files here
musiclist = ['catastrophe.mp3', 'beachlife.mp3', 'truefalse.mp3','bodys.mp3', 'ccf.mp3', 'connectdots.mp3', 'cutething.mp3', 'destroyedpowers.mp3', 'drunkdrivers.mp3', 'fillblank.mp3', 'Gethsemane.mp3', 'myboy.mp3', 'onlysex.mp3', 'po.mp3','runninghill.mp3','sleepingstrangers.mp3','soberdeath.mp3','statepark.mp3','sunburnedshirts.mp3','soberdeath.mp3','statepark.mp3','Vincent.mp3']

#this notifies the bot is online
@client.event
async def on_ready():
    print("Chanticleer is online")

@client.command(pass_context = True)
async def join(ctx):
    #this checks if the author is in voice call
    if (ctx.author.voice):
        #this chooses a random song in the list and plays it after joining
        chanticleerschoice = random.choice(musiclist)
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio(chanticleerschoice)
        player = voice.play(source)
        await ctx.send("I have joined vc")
        await ctx.send("now playing", chanticleerschoice)
    else:
        await ctx.send("You are not in a voice channel rn")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        #disconnect from the call
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I have left the voice channel")
    else:
        ctx.send("I am not in a voice channel rn")

#I dont remember what this does to be honest
@client.command(pass_context = True)
async def call(ctx):
    ctx.send("you called?")

#put your bots id here
client.run("")