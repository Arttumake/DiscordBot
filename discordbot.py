import discord
import os
import requests
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('alert'):
        await message.channel.send("This is an alert")

client.run(TOKEN)
print("Done")        