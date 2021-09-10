import os
import _thread
import json
import requests
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands
import websocket

TOKEN = os.getenv('DISCORD_TOKEN')
WEBHOOK_ID = os.getenv('PS2_WEBHOOKID')
WEBHOOK_TOKEN = os.getenv('PS2_WEBHOOK_TOKEN')
channel = 795640167229554732
alerts_cobalt = '{"service":"event","action":"subscribe","worlds":["13"],"eventNames":["MetagameEvent"]}'
logins = '{"service":"event","action":"subscribe","worlds":["13"],"eventNames":["PlayerLogin","PlayerLogout"]}'

bot = commands.Bot(command_prefix='!')
webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

@bot.event
async def on_ready():
	print('Online')
	await bot.get_channel(channel).send("hello")

def ws_message(ws, message):
	to_dict = json.loads(message)
	if "payload" in to_dict.keys():
		webhook.send("Alert", username='AlertsApp')
		print("================================")
		print("-------------ALERT--------------")
		print("================================")

def ws_open(ws):
	print("Opening...")
	ws.send(alerts_cobalt)
	
def on_error(ws, error):
	print(error)

def ws_thread():
	ws = websocket.WebSocketApp('wss://push.planetside2.com/streaming?environment=ps2&service-id=s:alerts', on_open=ws_open, on_message=ws_message)
	ws.run_forever()

_thread.start_new_thread(ws_thread, ())

count = 1
print("discorbot.py is now running")
bot.run(TOKEN)