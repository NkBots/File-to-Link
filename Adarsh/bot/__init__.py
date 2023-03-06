



import os
import os.path
from ..vars import Var
import logging
from pyrogram import Client

logger = logging.getLogger("bot")



StreamBot = Client(
    name="WebStreamer",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    
    plugins={"root": "Adarsh/bot/plugins"},
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}
