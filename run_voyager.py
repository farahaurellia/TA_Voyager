import os
import sys
from time import time
import requests

# ... (kode debug key kamu)
RAW_KEY = os.environ.get("OPENAI_API_KEY")
# Logika menunggu Bridge (Node.js) siap
bridge_ready = False
bridge_url = f"http://127.0.0.1:5000" # Sesuaikan variabel port-mu

print(f"--- Menunggu Bridge di {bridge_url} siap... ---")
for i in range(12): # Coba selama 60 detik (12 x 5 detik)
    try:
        # Voyager biasanya punya endpoint check atau kita coba hit portnya
        requests.get(bridge_url) 
        bridge_ready = True
        break
    except requests.exceptions.ConnectionError:
        print(f"--- Bridge belum siap, mencoba lagi dalam 5 detik... ({i+1}/12) ---")
        time.sleep(5)

if not bridge_ready:
    print("--- ERROR: Bridge gagal start setelah 60 detik. Mematikan bot. ---")
    sys.exit(1)

from voyager import Voyager

# Ganti angka di bawah dengan port yang muncul di Minecraft kamu
voyager = Voyager(
    mc_port=25565, 
    openai_api_key=RAW_KEY,
    action_agent_model_name="gpt-4o-mini",  
    critic_agent_model_name="gpt-4o-mini",
    server_port=5000,  # Ganti dengan port yang sama dengan yang digunakan di mineflayer/index.js
    resume=False
)

voyager.learn()