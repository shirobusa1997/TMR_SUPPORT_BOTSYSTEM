# ------------------------------------------------------
# Import Package Definition
# ------------------------------------------------------

import discord
import asyncio

# ------------------------------------------------------
# Reference File Definition
# ------------------------------------------------------

import info

# ------------------------------------------------------
# Main
#------------------------------------------------------

client = discord.Client()

@client.event
@asyncio.coroutine
def on_ready():
        print("-" * 20)
        print("Bot_Name :", client.user.name)
        print("Bot_ID   :", client.user.id)
        print("-" * 20)
        print("\nREADY")

@client.event
@asyncio.coroutine
def on_message(message):
        if client == message.author:
                return

        if message.content.startswith('!tanyao'):
                yield from client.send_file(client.get_server(SERVER_ID).default_channel, 'Resources/tanyao.png')

client.run(BOT_TOKEN)

