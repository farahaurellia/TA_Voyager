import multiprocessing
import sys
import json
from voyager import Voyager

def run_bot(config):
    # Inisialisasi HARUS di dalam fungsi ini agar setiap proses punya memori sendiri
    voyager = Voyager(
        mc_port=config["mc_lan_port"],
        server_port=config["server_port"], 
        ckpt_dir=config["ckpt_dir"],      # WAJIB beda agar tidak IO Error
        azure_login=None,                 # Lewati login Microsoft
        resume=False,                      # Mulai dari awal setiap kali
        openai_api_key="",
        mc_username=config["name"],
    )
    print(f"--- Memulai {config['name']} di Port {config['server_port']} ---")
    voyager.learn()

if __name__ == "__main__":
    mc_port = 60867 # Port LAN dari Minecraft Anda
    
    # Default konfigurasi bot
    default_bots = [
        {
            "name": "Bot_1",
            "server_port": 3002,
            "ckpt_dir": "ckpt/bot1",
            "mc_lan_port": mc_port
        },
        {
            "name": "Bot_2",
            "server_port": 3001,
            "ckpt_dir": "ckpt/bot2",
            "mc_lan_port": mc_port
        }
    ]
    
    # Baca konfigurasi dari command line arguments atau file
    bots = default_bots
    
    # Opsi 1: Baca dari file JSON jika argument diberikan
    if len(sys.argv) > 1:
        config_file = sys.argv[1]
        try:
            with open(config_file, 'r') as f:
                bots = json.load(f)
            print(f"✓ Konfigurasi dimuat dari: {config_file}")
        except FileNotFoundError:
            print(f"⚠ File {config_file} tidak ditemukan. Menggunakan konfigurasi default.")
            bots = default_bots
        except json.JSONDecodeError:
            print(f"⚠ Error parsing JSON. Menggunakan konfigurasi default.")
            bots = default_bots
    
    # Opsi 2: Baca dari command line arguments (nama bot dipisahkan dengan koma)
    # Contoh: python run_multi_voyager.py bot_names Agent_Alpha,Agent_Beta
    if len(sys.argv) > 2 and sys.argv[1] == "bot_names":
        bot_names = sys.argv[2].split(",")
        for i, name in enumerate(bot_names):
            if i < len(bots):
                bots[i]["name"] = name.strip()
        print(f"✓ Nama bot diubah: {[b['name'] for b in bots]}")

    processes = []
    for b_config in bots:
        # Menjalankan fungsi run_bot secara paralel
        p = multiprocessing.Process(target=run_bot, args=(b_config,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

