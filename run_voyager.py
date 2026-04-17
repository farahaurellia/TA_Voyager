import os
import sys

# PAKSA ambil dari environment OS dan cetak untuk bukti
RAW_KEY = os.environ.get("OPENAI_API_KEY")
if RAW_KEY:
    print(f"--- DEBUG TA: Python dapet key (10 digit): {RAW_KEY[:10]} ---")
    # Suntik ulang secara paksa ke environment sistem
    os.environ["OPENAI_API_KEY"] = RAW_KEY
else:
    print("--- DEBUG TA: Python BENERAN KOSONG gak dapet key ---")
    sys.exit(1) # Matikan biar gak error muter-muter

from voyager import Voyager

# Ganti angka di bawah dengan port yang muncul di Minecraft kamu
voyager = Voyager(
    mc_port=25565, 
    openai_api_key="",
    action_agent_model_name="gpt-4o-mini",  
    critic_agent_model_name="gpt-4o-mini",
    server_port=5000,  # Ganti dengan port yang sama dengan yang digunakan di mineflayer/index.js
    resume=False
)

voyager.learn()