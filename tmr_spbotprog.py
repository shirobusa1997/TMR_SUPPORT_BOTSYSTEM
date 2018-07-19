import discord
import asyncio

import ID_Information

client = discord.Client()

@asyncio.coroutine
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@asyncio.coroutine
def on_message(message):
	if message.content.startswith('!test'):
		counter = 0
		tmp = yield from client.send_message(message.channel, 'Calculating messages...')
		for log in client.logs_from(message.channel, limit = 100):
			if log.author == message.author:
				counter += 1

		yield from client.edit_message(tmp, 'You have {} messages.'.format(counter))
	elif message.content.startswith('!sleep'):
		yield from asyncio.sleep(5)
		yield from client.send_message(message.channel, 'Done sleeping')

	elif message.content.startswith('!greeting'):
		yield from client.send_message(message.channel, 'ほあようごぁいまーしゅ！')
		yield from client.send_message(message.channel, 'ほんほはほあようごぁいましゅといいたかったんしゅが、かちゅぜちゅがわるいためほあようごぁいまーしゅになってちまいまいた!')
	elif message.content.startswith('!hw'):
		yield from client.send_message(message.channel, 'Hello World.')

	elif message.content.startswith('タンヤオ') or message.content.startswith('断么九'):
		yield from client.send_file(client.get_server(SERVER_ID).default_channel, 'Resources/tanyao.png')

	elif message.content.startswith('!clanmatch'):
		counter = 0
		tmp = awai client.send_message(messafe.channel, 'Let\'s DICE !!!')
		for log in client.logs_from(messafe.channel, limit=100)
			if log.author == message.author:
				counter += 1

			yield from client.edit_message(tmp, 'You have {} messages.'. format(counter))
			
client.run(BOT_TOKEN)
