import os
import _thread
import json
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands
import websocket

TOKEN = os.getenv("DISCORD_TOKEN")  # required to start discord bot
WEBHOOK_ID = os.getenv("PS2_WEBHOOKID")
WEBHOOK_TOKEN = os.getenv("PS2_WEBHOOK_TOKEN")
PS2_SERVICE_ID = os.getenv("PS2_SERVICE_ID")

channel = 795640167229554732
alerts_cobalt = '{"service":"event","action":"subscribe","worlds":["13"],"eventNames":["MetagameEvent"]}'
continent_ids = {2: "Indar", 4: "Hossin", 6: "Amerish", 8: "Esamir", 10: "Oshur"}

bot = commands.Bot(command_prefix="!")
webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN, adapter=RequestsWebhookAdapter())

# websocket callback
def on_message(ws, message):
    payload_dict = json.loads(message)
    if "payload" not in payload_dict.keys() or "heartbeat" in payload_dict.values():
        return

    sub_dict = payload_dict["payload"]
    id = int(sub_dict["zone_id"])
    continent = continent_ids[id]
    # check for event type
    if sub_dict["metagame_event_state_name"] == "ended":
        print(f"Alert ended on {continent}")
        return
    elif sub_dict["metagame_event_state_name"] == "started":
        webhook.send(f"{continent} alert started", username="alertsApp")
        print("================================")
        print("-------------ALERT--------------")
        print("================================")
        print(message)
    else:
        print("Something went wrong")


def on_open(ws):
    print("Opening...")
    ws.send(alerts_cobalt)  # subscribe to event stream


def on_error(ws, error):
    print(error)


def websocket_thread():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://push.planetside2.com/streaming?environment=ps2&service-id=s:{PS2_SERVICE_ID}",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
    )
    ws.run_forever()


if __name__ == "__main__":
    _thread.start_new_thread(websocket_thread, ())
    print("discorbot.py is now running")
    bot.run(TOKEN)
