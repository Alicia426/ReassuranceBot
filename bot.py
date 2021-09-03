import discord
import os
import datetime
from secret import my_secret

client = discord.Client()

commands = ('!help', '!configure', '!hello', '!reassure',
            '!advice', '!config_stuffie', '!butter', '!tryout')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


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
        await message.channel.send('WIP 4')

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
        await message.channel.send('WIP 6')


while True:
    client.run(my_secret)
