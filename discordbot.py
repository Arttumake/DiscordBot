import os
import _thread
import json
from discord.ext import commands
import websocket

TOKEN = os.getenv('DISCORD_TOKEN')
channel = 795640167229554732
alerts_cobalt = '{"service":"event","action":"subscribe","worlds":["13"],"eventNames":["MetagameEvent"]}'
logins = '{"service":"event","action":"subscribe","worlds":["13"],"eventNames":["PlayerLogin","PlayerLogout"]}'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('Online')
	await bot.get_channel(channel).send("hello")

def ws_message(ws, message):
	print(f"Websocket: {message}")
	to_dict = json.loads(message)

	if "payload" in to_dict.keys():
		print("bot just announced")

def ws_open(ws):
	print("Opening...")
	ws.send(logins)
	
def on_error(ws, error):
	print(error)

def ws_thread():
	ws = websocket.WebSocketApp('wss://push.planetside2.com/streaming?environment=ps2&service-id=s:alerts', on_open=ws_open, on_message=ws_message)
	ws.run_forever()

_thread.start_new_thread(ws_thread, ())

count = 1
print("discorbot.py is now running")
bot.run(TOKEN)