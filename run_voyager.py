import os
import sys
import time
import requests

RAW_KEY = os.environ.get("OPENAI_API_KEY")
BRIDGE_URL = os.environ.get("BRIDGE_URL", "http://127.0.0.1:3000")
MC_PORT = int(os.environ.get("MC_PORT", "25565"))
SERVER_PORT = int(os.environ.get("SERVER_PORT", "3000"))

def wait_for_bridge(url, retries=24, delay=5):
    print(f"--- Menunggu Bridge di {url}/health siap... ---")
    for i in range(retries):
        try:
            r = requests.get(f"{url}/health", timeout=3)
            if r.status_code == 200:
                print("--- Bridge siap. ---")
                return True
            print(f"--- Bridge status {r.status_code}, retry... ({i+1}/{retries}) ---")
        except requests.exceptions.RequestException as e:
            print(f"--- Bridge belum siap ({i+1}/{retries}): {e} ---")
        time.sleep(delay)
    return False

if not RAW_KEY:
    print("--- ERROR: OPENAI_API_KEY tidak ditemukan. ---")
    sys.exit(1)

if not wait_for_bridge(BRIDGE_URL):
    print("--- ERROR: Bridge gagal start. ---")
    sys.exit(1)

from voyager import Voyager

# Ganti angka di bawah dengan port yang muncul di Minecraft kamu
voyager = Voyager(
    mc_port=25565, 
    openai_api_key=RAW_KEY,
    action_agent_model_name="gpt-4o-mini",  
    critic_agent_model_name="gpt-4o-mini",
    server_port=SERVER_PORT,  # Ganti dengan port yang sama dengan yang digunakan di mineflayer/index.js
    resume=False
)

voyager.learn()