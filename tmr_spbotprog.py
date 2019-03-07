# ------------------------------------------------------
# Import Package Definition
# ------------------------------------------------------

import discord
import asyncio

# ------------------------------------------------------
# Reference File Definition
# ------------------------------------------------------

from info import *

# ------------------------------------------------------
# Main
#------------------------------------------------------

client = discord.Client()

@client.event
async def on_ready():
        print("-" * 20)
        print("Bot_Name :", client.user.name)
        print("Bot_ID   :", client.user.id)
        print("-" * 20)
        print("\nREADY")

@client.event
async def on_message(message):
        if client == message.author:
            return

        if message.content.startswith('!tanyao'):
            await client.send_file(message.channel, 'Resources/tanyao.png')

client.run(BOT_TOKEN)
