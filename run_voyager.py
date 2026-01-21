from voyager import Voyager

# Ganti angka di bawah dengan port yang muncul di Minecraft kamu
voyager = Voyager(
    mc_port=51234, 
    openai_api_key="",
    action_agent_model_name="gpt-4o-mini",  
    critic_agent_model_name="gpt-4o-mini"
)

voyager.learn()