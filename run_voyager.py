import os
from dotenv import load_dotenv

# 1. Coba load dari .env (jika ada)
load_dotenv()

# 2. Ambil dari environment system (yang dikirim Coolify)
api_key = os.getenv("OPENAI_API_KEY")

# 3. DEBUG: Print untuk memastikan (Opsional, hapus jika sudah jalan)
if api_key:
    print(f"Python berhasil baca Key: {api_key[:10]}...")
else:
    print("Python GAGAL baca Key dari os.getenv")

# 4. PAKSA masukkan ke environment agar dibaca LangChain/Pydantic
os.environ["OPENAI_API_KEY"] = api_key

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