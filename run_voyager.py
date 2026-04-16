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