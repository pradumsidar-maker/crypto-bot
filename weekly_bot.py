import requests, asyncio
from datetime import datetime, timedelta, timezone
from telegram import Bot

# ===== CONFIG =====
TOKEN = "8690174599:AAEMuipJVajwkZaBBsoPxsor-c1H3NxdP3M"
CHAT_ID = "5270697473"

COINS = [
    "BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","XRPUSDT",
    "ADAUSDT","DOGEUSDT","MATICUSDT","DOTUSDT","AVAXUSDT",
    "LTCUSDT","TRXUSDT","SHIBUSDT","UNIUSDT","ATOMUSDT",
    "LINKUSDT","XLMUSDT","FTMUSDT","NEARUSDT","ALGOUSDT"
]

bot = Bot(token=TOKEN)

# alert status
triggered = {
    coin: {"high": False, "low": False, "open": False, "close": False, "zone": False}
    for coin in COINS
}

# ===== WEEK RESET =====
def next_week_reset():
    now = datetime.now(timezone.utc)
    next_monday = now + timedelta(days=(7 - now.week
