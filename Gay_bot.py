import discord
import requests
import json
import random

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Lô cc!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('gay'):
        await message.channel.send('gay cái dkmm')

    if message.content.startswith(':wjbudrink:'):
        await message.channel.send('tí tuổi đầu đã đòi uống rượu ?')

    actionate = discord.Activity(name='Yuri and Lesbian', type=discord.ActivityType.watching)
    await client.change_presence(status=discord.Status.idle, activity=actionate)
client.run('ODEwMTQyMTcxMzkwODA0MDA5.YCfVsQ.OFcFM4OEskMFtgeTCVLF6HMwo2k')

