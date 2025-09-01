# config.py
import os

# ---- Güvenlik anahtarı (TradingView JSON "key" ile eşleşecek) ----
sec_key = os.getenv("SECRET_KEY", "")  # Heroku'daki SECRET_KEY'i okur

# ---- Telegram ayarları ----
send_telegram_alerts = True
tg_token = os.getenv("BOT_TOKEN", "")
channel = int(os.getenv("CHAT_ID", "0"))

# Diğer servisler aynı kalsın (discord/slack/twitter/email = False)
