import os
import sys
import requests
import platform
import socket

BOT_TOKEN = "9256925118:AAFPvwtbnizucI_X-8UlyvAJrXKlSDNIKRY"
CHAT_ID = "6947664268"

def get_system_telemetry():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "127.0.0.1"
    
    return {
        "platform": platform.platform(),
        "hostname": hostname,
        "ip": ip_address,
        "machine": platform.machine()
    }

def send_telegram_alert(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, json=payload, timeout=10)
        print(f"[DEBUG] Telegram API Response Code: {response.status_code}")
        print(f"[DEBUG] Telegram API Response Body: {response.text}")
        return response.json()
    except Exception as e:
        print(f"[-] Connection Error: {e}")

if __name__ == "__main__":
    print("[+] Testing Telegram Bot Connection...")
    telemetry = get_system_telemetry()
    report = f"💎 *Kurd Call Center Test*\n\nHost: `{telemetry['hostname']}`\nIP: `{telemetry['ip']}`"
    send_telegram_alert(report)
