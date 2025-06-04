import requests

BOT_TOKEN = "8000286711:AAFiFXs6qjXh2nL11xpwynRSc-lAhkElQr8"
CHAT_ID = "6217477088"
TEXT = "✅ Abaqus Job-test.inp is ready for simulation."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": TEXT}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("📲 Telegram notification sent to your phone.")
else:
    print("❌ Failed to send Telegram message:", response.text)
