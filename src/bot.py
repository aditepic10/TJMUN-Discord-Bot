import os
import time

import discord  # pip install discord.py
from dotenv import load_dotenv  # .env for discord token

load_dotenv()  # load .env for discord token
TOKEN = os.getenv('DISCORD_TOKEN')  # extract discord token

client = discord.Client()  # open up discord client

"""Checks if bot is ready and prints a message"""


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


"""Checks for messages and responds based on word count"""


# TODO: Forward to chair's DMs and only allow successful directive requests within 10 mins of the first
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    words = len(message.content.split(" "))  # get string contents and split by space to get word count
    if words > 100:
        response = "Sorry, your directive is too long. Please shorten it and send another message"
    else:
        response = "Thank you, your directive has been received."
        czar = client.get_user(405839490251227138)  # Adit's discord ID (yours can be found by enabling dev mode and
        # r-clicking your user name
        crisis_message = "NEW MESSAGE FROM {}\n".format(message.author) + message.content
        await czar.send(crisis_message)  # if the message passes the tests, send it over to crisis.

    await message.channel.send(response)


client.run(TOKEN)
