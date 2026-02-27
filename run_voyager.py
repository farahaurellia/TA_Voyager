from voyager import Voyager

# Ganti angka di bawah dengan port yang muncul di Minecraft kamu
voyager = Voyager(
    mc_port=54320, 
    openai_api_key="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",
    action_agent_model_name="gpt-4o-mini",  
    critic_agent_model_name="gpt-4o-mini"
)

voyager.learn()