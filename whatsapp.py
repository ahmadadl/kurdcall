import os
import sys
import time
import requests

BOT_TOKEN = "9011362716:AAHu7AJ1P7dEZCMfs0Mhu8B2U-Df0XnYOOQ"
CHAT_ID = "6947664268"

def send_telegram_alert(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("[+] Kurd Call Center Forensic Engine Secured...")
    send_telegram_alert("💎 *Kurd Call Center Secured* - Target Connected via WhatsApp Telemetry!")
