import discord
import asyncio

import info

client = discord.Client()

@client.event
async def on_ready():
	print('READY')

@client.event
async def on_message(message):
	if client == message.author:
		return

	if message.content.startswith("タンヤオ"):
		await client.send_file(message.channel, 'Resources/tanyao.png')

client.run(info.BOT_TOKEN)
