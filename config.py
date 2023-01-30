# (  )Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5773373505:AAFxQuJ6klB7bVd-30n1XVvQi87DaTKVLXk")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7375040"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "4166e18db5a7880136d41ceb0aa20971")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001836566126"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1880970848"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Vidraplay")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://vvjolkjp:zBgJLBKi7m0FPyXtVt6djFV1YeCOUooD@satao.db.elephantsql.com/vvjolkjp")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "ometvi")
GROUP = os.environ.get("GROUP", "Huntersxyz")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001787258151"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "-1001733683757"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
