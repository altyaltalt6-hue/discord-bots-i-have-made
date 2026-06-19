import discord
from discord.ext import commands
import time
import random
import os

swears =0

#pSetup Intents (Required to read message content)
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix= "chant" ,intents=intents)

checks = 1

counts = 0
#for censorship purposes, this is blank. This list basically is the words that the bot detects
SWEARS = []
#this lets you know when the bot is online
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    #do the channel announcement here, in messingwithbots probably
    
#main thingy

@client.event
async def on_message(message):
    global swears
    global user

    message_content = message.content.lower()

    if message.author == client.user:
        return
    

    if any(trigger in message_content for trigger in SWEARS):
        global counts
        counts = 0
        user_id = message.author.id
        try:
            user = await client.fetch_user(user_id)
            print(f"Found user: {user.name}")
        except discord.NotFound:
            print("User could not be found.")
        except discord.HTTPException:
            print("Failed to connect to Discord API.")


            
        with open(f"{user.name}.txt", "a") as file:
        #i genuinely don't know how i did this, i was half asleep, but it still works lol
            repeat = len(SWEARS)
            for repeat in range(repeat):
                amount = message_content.count(SWEARS[counts])
                for amount in range(amount):
                    file.write(f"{message_content}\n")
                counts +=1

        with open(f"{user.name}.txt", "r") as file:
            for line in file:
                swears +=1
        await message.channel.send(f"Please stop swearing. {swears} swears sworn")
        swears = 0


    #this lets you see how many swears you have
        user_id = message.author.id
        try:
            user = await client.fetch_user(user_id)
            print(f"Found user: {user.name}")
        except discord.NotFound:
            print("User could not be found.")
        except discord.HTTPException:
            print("Failed to connect to Discord API.")
            
        await message.channel.send("You are forgiven")

        os.remove(f"{user.name}.txt")
    if message.content.lower() == "what's my swear count":
        user_id = message.author.id
        try:
            user = await client.fetch_user(user_id)
            print(f"Found user: {user.name}")
        except discord.NotFound:
            print("User could not be found.")
        except discord.HTTPException:
            print("Failed to connect to Discord API.")
        with open(f"{user.name}.txt", "a") as file:
            print(f"File Opened, {user.name}")
        with open(f"{user.name}.txt", "r") as file:
                    for line in file:
                        swears +=1
        await message.channel.send(f"Please stop swearing. {swears} swears sworn")
        swears = 0
    swears = 0

#put your bot code here
client.run('')
