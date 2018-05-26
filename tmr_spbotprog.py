import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!test'):
		counter = 0
		tmp = await client.send_message(message.channel, 'Calculating messages...')
		async for log in client.logs_from(message.channel, limit = 100):
			if log.author == message.author:
				counter += 1

		await client.edit_message(tmp, 'You have {} messages.'.format(counter))
	elif message.content.startswith('!sleep'):
		await asyncio.sleep(5)
		await client.send_message(message.channel, 'Done sleeping')

	elif message.content.startswith('!greeting'):
		await client.send_message(message.channel, 'ほあようごぁいまーしゅ！')
		await client.send_message(message.channel, 'ほんほはほあようごぁいましゅといいたかったんしゅが、かちゅぜちゅがわるいためほあようごぁいまーしゅになってちまいまいた!')
	elif message.content.startswith('!hw'):
		await client.send_message(message.channel, 'Hello World.')

	elif message.content.startswith('タンヤオ') or message.content.startswith('断么九'):
		await client.send_file(client.get_server('<REPLACE TO TARGET SERVER ID>').default_channel, 'Resources/tanyao.png')

	elif message.content.startswith('!clanmatch'):
		counter = 0
		tmp = awai client.send_message(messafe.channel, 'Let\'s DICE !!!')
		async for log in client.logs_from(messafe.channel, limit=100)
			if log.author == message.author:
				counter += 1

			await client.edit_message(tmp, 'You have {} messages.'. format(counter))
			
client.run('<REPLACE TO BOT TOKEN>')
