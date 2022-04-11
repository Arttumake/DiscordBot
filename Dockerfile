FROM python:3.9
WORKDIR /PS2DiscordBot
ENV DISCORD_TOKEN=Nzk1NjM5ODY3OTA3NzY4MzIx.X_MTXg.9MX8gCVYVhblk5qNflyvG5YGjKE
ENV PS2_WEBHOOKID=885934016279216139
ENV PS2_WEBHOOK_TOKEN=aYNSljTpPsOkmF3PDm4Jji4-EqndMfV6WtY3kU8DkwJEi2CvpONS2mdC8oK8HIL0m5jR
ENV PS2_SERVICE_ID=s:cobaltalert
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD [ "python3", "discordbot.py"]
