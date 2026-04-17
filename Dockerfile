# Menggunakan base image yang sudah punya Python dan Node sekaligus
FROM nikolaik/python-nodejs:python3.11-nodejs20

WORKDIR /app

# Install dependencies Node (Bridge)
COPY voyager/env/mineflayer/package.json ./voyager/env/mineflayer/
RUN cd voyager/env/mineflayer && npm install

# 2. PAKSA instalasi modul biang kerok langsung di layer Docker
# Ini memastikan modul-modul ini ada sebelum sisa requirements dijalankan
# Tambahkan tanda kutip di sekeliling pydantic<2.0
RUN pip install --no-cache-dir \
    "gymnasium==0.28.1" \
    "minecraft-launcher-lib==8.0" \
    "psutil" \
    "langchain-community" \
    "langchain-openai" \
    "pydantic<2.0"

# Install dependencies Python (Voyager)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy sisa kode
COPY . .

# Script untuk menyalakan Bridge lalu Bot secara berurutan
CMD node voyager/env/mineflayer/index.js $SERVER_PORT $MC_PORT $MC_HOST $BOT_NAME & sleep 60 && python run_voyager.py
