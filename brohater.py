import discord
from discord.ext import commands
import time
import random

#pSetup Intents (Required to read message content)
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix= "chant" ,intents=intents)

checks = 1



jokes = ['Did you hear about the circus fire? It was in tents!','How do you catch a squirrel? Climb a tree and act like a nut!','Did you hear about the guy who invented Lifesavers? They say he made a mint!','I told my wife she should embrace her mistakes. She gave me a hug.','Why dont eggs tell jokes? They might crack up!','What did the big flower say to the little flower? "Hi, bud!"','I went to buy some camouflage pants, but I couldnt find any.','What did the grape say when it got stepped on? Nothing, it just let out a little wine.','I used to have a job at a calendar factory, but I got fired because I took a couple of days off.','What do you call a snowman with a six-pack? An abdominal snowman!','Why dont skeletons fight each other? They dont have the guts!','Did you hear about the restaurant on the moon? Great food, no atmosphere!','What did one wall say to the other wall? Ill meet you at the corner!','Why did the math book look sad? Because it had too many problems!','What did one hat say to the other hat? You stay here, Ill go on ahead!','Why did the coffee file a police report? It got mugged!','I was going to tell you a joke about time travel, but you didnt like it.','I used to be a baker, but I couldnt make enough dough.','Did you hear about the guy who got hit in the head with a can of soda? He was lucky it was a soft drink.','Im writing a book about glue, but Im stuck on the first chapter.','What did one plate whisper to the other plate? Dinner is on me.','Why did the golfer bring two pairs of pants? In case he got a hole in one.’,‘Two sheep walk into a—baaaa.','Stop looking for the perfect match; use a lighter.','Try the seafood diet—you see food, then you eat it.','Did you hear the rumor about butter? Well, Im not going to go spreading it!','Whats Forrest Gumps password? 1forrest1','What state is known for its small drinks? Minnesota.','What does a nosey pepper do? It gets jalapeño business.','I have a clean conscious—its never been used.','I love telling Dad jokes. Sometimes, he even laughs.']








mode2 = 0


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    #do the channel announcement here, in messingwithbots probably
    

@client.event
async def on_message(message):
    global checks
    global mode2
    global channel22
    #ignore messages from the bot

    #this is used to check if you have a role,copy the id for it. 
    role = message.guild.get_role()

    if message.author == client.user:
        return
    #this checks to see if the user has the right role to speak to the bot
    if role in message.author.roles:
        #this checks to see if checks isnt 1, checks is changed through text triggers (i didnt know how commands worked at the time)
        if checks == 1:
            #this is my bot's name, pick your own or keep it if you want
            if "chanticleer".lower() in message.content.lower():
                await message.channel.send("thats me!!")
        
        #i made this before i learnt about actual commands, but it still turns the bot on/off
        if "!turn off".lower() in message.content.lower():
            checks = 2
            await message.channel.send("okay see ya!")   

        if "!turn on".lower() in message.content.lower():
            checks = 1
            await message.channel.send("hi everybody!")   
        #checks if the bot is on
        if "!check".lower() in message.content.lower():
            if checks == 2:
                await message.channel.send("I am not sending messages right now!")    
            if checks == 1:

                await message.channel.send("I'm online!")   
        #tells a random joke
        if "! joke".lower() in message.content.lower():
            await message.channel.send(random.choice(jokes))






#put your bots id here to use this!
client.run('')
