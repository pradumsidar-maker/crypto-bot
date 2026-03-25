import os
import time
from telegram import Bot
from flask import Flask
import threading

# ===== TELEGRAM SETUP =====
BOT_TOKEN = os.getenv("8690174599:AAEMuipJVajwkZaBBsoPxsor-c1H3NxdP3M")
CHAT_ID = os.getenv("5270697473")

bot = Bot(token=BOT_TOKEN)

# ===== TEST MESSAGE =====
try:
    bot.send_message(chat_id=CHAT_ID, text="🚀 Bot Started Successfully!")
except Exception as e:
    print("Telegram Error:", e)

# ===== LOOP (RUNNING CHECK) =====
def run_bot():
    while True:
        print("Bot is running...")
        time.sleep(60)

# ===== FLASK SERVER (FOR RENDER FREE) =====
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_web():
    app.run(host="0.0.0.0", port=10000)

# ===== RUN BOTH =====
threading.Thread(target=run_web).start()
run_bot()
