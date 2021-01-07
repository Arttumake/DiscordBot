import discord
import os
import requests
import asyncio
from websocket import create_connection
import time
import json
from dotenv import load_dotenv

#client = discord.Client()
load_dotenv()
cobalt_alert = {
	"service":"event",
	"action":"subscribe",
	"worlds":["13"],
	"eventNames":["FacilityControl",
	"MetagameEvent"]
}

TOKEN = os.getenv('DISCORD_TOKEN')

ws = create_connection("wss://push.planetside2.com/streaming?environment=ps2&service-id=s:alerts")

ws.send('{"service":"event","action":"subscribe","worlds":["1"],"eventNames":["PlayerLogin","PlayerLogout"]}')

while True:
    msg = ws.recv()
    print(msg)