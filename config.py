from os import getenv

from dotenv import load_dotenv

admins = {}

load_dotenv()

# client vars

API_ID = int(getenv("9198094"))

API_HASH = getenv("5873984ba5ad6873afcb9b19df393dc9")

BOT_TOKEN = getenv("5871562228:AAEG3currbmEajQFLYsuwhxvvDnAUw2WWvA")

SESSION_NAME = getenv("SESSION_NAME", "AgArzOnBYH8F7htGG-9hfLAxBasGUmxHow-2R0YgL2IeHpXwzBtsjg9CYPvBZEJ4afJL4bV_JpTbdRdDr6fYEU0tFO3CbH97edljVaSTm9MvOpe5xnV8JHZAw7jkGCl59-9Id8R2Zk0nx0-M1QjYSwZeZjSn_K1p0XVBq7tzxcGkdNodPGy9t-hTqC8zY_xEZDrtc7VloflN6K6ZFEv1EPIz7pTesvH0JwwrV36oZJbeFttrvSNZ4MK64JxnSHGRqJ9QX0M6vup8_f8d0dRZCFa_LAo9HX9uDHRuNELqyLoI1_71TgO0tRqzOokNH0B5lowaOfEwcDNc-uIIQuMQ1NInAAAAAT9EPpQA")

# mandatory vars

OWNER_USERNAME = getenv("OWNER_u7010")

ALIVE_NAME = getenv("mahde")

BOT_USERNAME = getenv("u7010bot")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")

UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))

GROUP_SUPPORT = getenv("ovvvei", "VeezSupportGroup")

UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QMWMW")

# database, decorators, handlers mandatory vars

MONGODB_URL = getenv("mongodb+srv://veez:mega@cluster0 .heqnd.mongodb.net/veez?retryWrites= true&w=majority")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())

OWNER_ID = list(map(int, getenv("5598607769").split()))

SUDO_USERS = list(map(int, getenv("5598607769").split()))

# image resources vars

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")

IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")

IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")

IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")

IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")

ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
