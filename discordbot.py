from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import asyncio
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == f'{PREFIX}야':
        await message.channel.send("뭐")

    if message.content.startswith(f'{PREFIX}안녕'):
        await message.channel.send(':wave:')
        
    if message.content.startswith(f"{PREFIX}타이머"):
        word = message.content.split()
        word_count = len(word)
        print(word)
        
        if word_count == 2:
            asyncio.sleep(word[2])
            message.content.send(f"{message.author.mention}, {word[2]}초가 지났어요!")


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
