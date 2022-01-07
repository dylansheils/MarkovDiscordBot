import sys
import os
import subprocess
import time
from os import listdir
from os.path import isfile, join

# Just for future convience
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("discord")
install("markovify")
import markovify

person = "Shelly"
totalPath = "./" + person + "/"
articles = [f for f in listdir(totalPath) if isfile(join(totalPath, f))]
articlesContent = ""

modelDylan = ""
modelShelly = ""
modelWilliam = ""
modelEric = ""
modelLiam = ""
modelGabriel = ""
modelColin = ""
modelDaniel = ""
modelMadeline = ""
modelLily = ""
modelCS = ""
count = 1
for article in articles:
    if ".txt" in article:
        if "Study Gang" in article:
            fileObj = open(totalPath + article, encoding='utf-8')
            lines = fileObj.readlines()
            getNextLine = False
            prior = ""
            for line in lines:
                if getNextLine:
                    if "dalearn#5106" in prior:
                        modelWilliam += line.replace('\n', '') + ". "
                    if "dylansheils0241#7218" in prior:
                        modelDylan += line.replace('\n', '') + ". "
                    if "sbels#3430" in prior:
                        modelShelly += line.replace('\n', '') + ". "
                    if "PotatoPalooza#8058" in prior:
                        modelEric += line.replace('\n', '') + ". "
                    if "GabrielJC20#7186" in prior:
                        modelGabriel += line.replace('\n', '') + ". "
                    if "sbts#8517" in prior:
                        modelLiam += line.replace('\n', '') + ". "
                    if "cxider#1396" in prior:
                        modelColin += line.replace('\n', '') + ". "
                    if "EnthusiastiCat#2609" in prior or "MelodyLine#4239" in prior:
                        modelMadeline += line.replace('\n', '') + ". "
                    if "Danecchio#1773" in prior:
                        modelDaniel += line.replace('\n', '') + ". "
                    if "lily.ritt#0001" in prior:
                        modelLily += line.replace('\n', '') + ". "
                    modelCS += line.replace('\n', '') + ". "
                    getNextLine = False
                if "[" in line:
                    prior = line
                    getNextLine = True
        else:
            if "Gabriel" in article:
                fileObj = open(totalPath + article, encoding='utf-8')
                lines = fileObj.readlines()
                getNextLine = False
                prior = ""
                for line in lines:
                    modelGabriel += line.replace('\n', '') + ". "
            else:
                if "[" in article:
                    fileObj = open(totalPath + article, encoding='utf-8')
                    lines = fileObj.readlines()
                    getNextLine = False
                    prior = ""
                    for line in lines:
                        if getNextLine:
                            if "EnthusiastiCat#2609" in prior or "MelodyLine#4239" in prior:
                                modelMadeline += line.replace('\n', '') + ". "
                            getNextLine = False
                        if "[" in line:
                            prior = line
                            getNextLine = True
                else:
                    fileObj = open(totalPath + article, encoding='utf-8')
                    lines = fileObj.readlines()
                    getNextLine = False
                    prior = ""
                    for line in lines:
                        modelDylan += line.replace('\n', '') + ". "
        count += 1
    print("Progress: ", count/len(articles))



modelDylan = markovify.Text(modelDylan, state_size=2)
modelShelly = markovify.Text(modelShelly, state_size=2)
modelWilliam = markovify.Text(modelWilliam, state_size=2)
modelEric = markovify.Text(modelEric, state_size=2)
modelLiam = markovify.Text(modelLiam, state_size=2)
modelGabriel = markovify.Text(modelGabriel, state_size=2)
modelColin = markovify.Text(modelColin, state_size=2)
modelDaniel = markovify.Text(modelDaniel, state_size=2)
modelMadeline = markovify.Text(modelMadeline, state_size=2)
modelLily = markovify.Text(modelLily, state_size=2)
modelCS = markovify.Text(modelCS, state_size=2)
print("Made the Models!")

import os
import random
import time
from discord.ext import commands
import discord

TOKEN = "OTI5MDg3MjEzMDAbuyyBNTY4.YdiN5Q.fREPeVgrBf4ot6mRF_p2EyOflN0"

bot = commands.Bot(command_prefix=("!"))
client = discord.Client()

import random
count = 0
botsToPick = ['CSBot', 'DylanBot', 'WilliamBot', 'ShellyBot', 'EricBot', 'LiamBot', 'GabrielBot', 'ColinBot', 'DanielBot', 'MadelineBot', 'LilyBot']
class OurBot(commands.Cog):
    def init(self, bot):
        self.bot = bot
        print("Bot in Server")

    @commands.Cog.listener() #Let's not be antisocial
    async def on_message(self, message):
        global count
        if message.author.bot:
            return  # ignore bots
        if 'BotBot' in message.content:
            num1 = random.randint(0, 10)
            num2 = random.randint(0, 10)
            count += 1
            message.content += '    BotBot: ' + botsToPick[num1] + ' ' + botsToPick[num2]
        if 'CSBot' in message.content:
            sentence = ""
            sentence = 'CSBot: ' + str(modelCS.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'DylanBot' in message.content:
            sentence = ""
            sentence = 'DylanBot: ' + str(modelDylan.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'WilliamBot' in message.content:
            sentence = ""
            sentence = 'WilliamBot: ' + str(modelWilliam.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'ShellyBot' in message.content:
            sentence = ""
            sentence = 'ShellyBot: ' +str(modelShelly.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'EricBot' in message.content:
            sentence = ""
            sentence = 'EricBot: ' + str(modelEric.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'LiamBot' in message.content:
            sentence = ""
            sentence = 'LiamBot: ' + str(modelLiam.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'GabrielBot' in message.content:
            sentence = ""
            sentence = 'GabrielBot: ' + str(modelGabriel.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'ColinBot' in message.content:
            sentence = ""
            sentence = 'ColinBot: ' + str(modelColin.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'DanielBot' in message.content:
            sentence = ""
            sentence = 'DanielBot: ' + str(modelDaniel.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'MadelineBot' in message.content:
            sentence = ""
            sentence = 'MadelineBot: ' + str(modelMadeline.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'LilyBot' in message.content:
            sentence = ""
            sentence = 'LilyBot: ' + str(modelLily.make_sentence())
            await message.channel.send(sentence, reference=message)
        if 'fail' in message.content:
            await message.channel.send("Yeah, right, have some more confidence :D! Also, STOP CAPPING!")
        if 'test' in message.content:
            await message.channel.send("Wait, there was a test today?")
        if 'COVID' in message.content:
            await message.channel.send("Make sure to kiss the homies!")
        if 'depressed' in message.content:
            await message.channel.send("Be happy! :D")
        if 'stressed' in message.content:
            await message.channel.send("Relax, man, it will all be good")
        if 'duck' in message.content:
            await message.channel.send("Dylan REALLY loves ducks, like that man sleeps with them...fucking weirdo")
        if 'happy' in message.content:
            await message.channel.send("Me too")

bot.add_cog(OurBot(bot))
bot.run(TOKEN)

print("DONE")
