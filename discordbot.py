import discord
import os
import time
import _thread
import json
from websocket import create_connection
from dotenv import load_dotenv
import websocket


#client = discord.Client()
load_dotenv()
cobalt_alert = {
	"service":"event",
	"action":"subscribe",
	"worlds":"13",
	"eventNames":"MetagameEvent"
}

alerts_cobalt = '{"service":"event","action":"subscribe","worlds":["13"],"eventNames":["MetagameEvent"]}'
logins = '{"service":"event","action":"subscribe","worlds":["1"],"eventNames":["PlayerLogin","PlayerLogout"]}'
TOKEN = os.getenv('DISCORD_TOKEN')
#Websocket callback functions

def ws_message(ws, message):
	print(f"Websocket: {message}")
	to_dict = json.loads(message)
	if "payload" in to_dict.keys():
		print("this is a payload")

def ws_open(ws):
	ws.send(alerts_cobalt)

def ws_thread(*args):
	ws = websocket.WebSocketApp('wss://push.planetside2.com/streaming?environment=ps2&service-id=s:alerts', on_open=ws_open, on_message=ws_message)
	ws.run_forever()

_thread.start_new_thread(ws_thread, ())
count = 1
print("discorbot.py is now running")
while True:
	time.sleep(60)
	print(f"Main thread: online for {count} minutes")
	count += 1