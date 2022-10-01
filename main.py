import discord
from web_scraper import *
import os
from discord.ext import tasks 



intents = discord.Intents.all()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  channel = client.get_channel(1025228911551987824)
  await channel.send('hello')

  mytask.start()

  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

@tasks.loop(seconds=60)
async def mytask():
  link = await Web_scraper()
  print(link)
  if link != "false":
    channel = client.get_channel(1025228911551987824)
    await channel.send(link)

client.run('MTAyNTIyNTU4Nzg5MzIxNTMyMw.GLlhEg.6kgyS0FRDYrlzgD02QTPUUziLxOmyoBa06N5Z4')
