FROM nikolaik/python-nodejs:python3.11-nodejs20

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/voyager/env/mineflayer
RUN npm install

WORKDIR /app

RUN printf '%s\n' \
'#!/usr/bin/env bash' \
'set -e' \
'' \
'export SERVER_PORT="${SERVER_PORT:-3000}"' \
'export MC_PORT="${MC_PORT:-25565}"' \
'export MC_HOST="${MC_HOST:-127.0.0.1}"' \
'export BOT_NAME="${BOT_NAME:-bot}"' \
'export BRIDGE_URL="http://127.0.0.1:${SERVER_PORT}"' \
'' \
'' \
'python /app/run_voyager.py' \
'' \
> /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"]