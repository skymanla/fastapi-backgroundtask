import os
import sys
import asyncio
import datetime
import json
import requests
from fastapi import FastAPI, BackgroundTasks
from app.config import EnvSetting

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

app = FastAPI()

config = EnvSetting()


def kst_maker():
    now = datetime.datetime.now(datetime.timezone.utc)
    korea_time = now.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
    timestamp = korea_time.timestamp()
    int_timestamp = int(timestamp)
    dt = datetime.datetime.fromtimestamp(int_timestamp)
    return dt


async def send(message):
    slack_url = 'https://hooks.slack.com/services/slackurl'
    slack_channel = '#web-hook'
    user_name = 'Bot'
    kst_time = kst_maker()
    _data = {
        "text": message + f"(time: {kst_time})",
        "channel": slack_channel,
        "username": user_name
    }
    requests.post(
        url=slack_url,
        data=json.dumps(_data),
        headers={'Content-Type': 'application/json'}
    )


async def get_health():
    while True:
        try:
            requests.get(f"""http://{config.URL}/health""")
        except Exception as e:
            await send(f"""{config.ENV} 서버 다운""")
        finally:
            await asyncio.sleep(10)


@app.on_event("startup")
async def on_app_startup():
    loop = asyncio.get_event_loop()
    loop.create_task(get_health())