import discord
import os
import datetime
import random
import ymldb
from secret import my_secret
from advice import advice_list
from tryout import tryout_string
from reassurance import reassurances

client = discord.Client()

commands = ('!help', '!configure', '!hello', '!reassure',
            '!advice', '!config_stuffie', '!butter', '!tryout')


def pronounParser(pronoun_string):
    pronouns = pronoun_string.strip().split("/")
    pronoun_dict = {
        "sps": pronouns[0], "spo": pronouns[1], "sp": pronouns[2], "sr": pronouns[3]}
    return pronoun_dict


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("I know", len(advice_list), "pieces of advice.")
    print("I have", len(reassurances), "reassurance affimations")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Help Text
    if message.content.startswith(commands[0]):
        print(message.content, message.author)
        with open('helptext.txt', 'r') as file:
            data = file.read()
            await message.channel.send(data)

    # Configures user name and pronouns
    if message.content.startswith(commands[1]):
        print(message.author, message.content)
        name = message.content.split(" ")[1]
        pronouns = pronounParser(message.content.split(" ")[2])
        print(name, pronouns)
        await message.channel.send('WIP 1')

    # Says hello
    if message.content.startswith(commands[2]):
        print(message.author, message.content)
        await message.channel.send('Hello! I am working fine! \n Thank you for checking in on me.')

    # Reassures user or stufie
    if message.content.startswith(commands[3]):
        print(message.author, message.content)
        await message.channel.send('WIP 3')

    # Gives life advice
    if message.content.startswith(commands[4]):
        print(message.author, message.content)
        adv = random.choice(advice_list)
        await message.channel.send(adv)

    # Gives life advice
    if message.content.startswith(commands[5]):
        print(message.author, message.content)
        await message.channel.send('WIP 5')

    # Passes butter
    if message.content.startswith(commands[6]):
        print(message.content, message.author)
        with open('butter.txt', 'r') as file:
            data = file.read()
            await message.channel.send(data)

    # Try name and pronouns out
    if message.content.startswith(commands[7]):
        print(message.content, message.author)
        name = message.content.split(" ")[1]
        pronouns = pronounParser(message.content.split(" ")[2])
        print(name, pronouns)
        if pronouns["sps"] == "they":
            s = ""
            spob = "their"
        else:
            spob = pronouns["spo"]
            s = "s"
        msg = tryout_string.format(spob=spob,
                                   name=name,
                                   spo=pronouns["spo"],
                                   sps=pronouns["sps"],
                                   sp=pronouns["sp"],
                                   sr=pronouns["sr"],
                                   s=s)
        await message.channel.send(msg)


while True:
    client.run(my_secret)
