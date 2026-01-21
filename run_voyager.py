from voyager import Voyager

# Ganti angka di bawah dengan port yang muncul di Minecraft kamu
voyager = Voyager(
    mc_port=51234, 
    openai_api_key="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",
    action_agent_model_name="gpt-4o-mini",  
    critic_agent_model_name="gpt-4o-mini"
)

voyager.learn()