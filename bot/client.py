from binance.client import Client
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

env_path = os.path.join(
    BASE_DIR,
    ".env"
)

load_dotenv(env_path)

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

if not API_KEY or not API_SECRET:
    raise ValueError(
        "API_KEY or API_SECRET not found in .env"
    )

client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET,
    testnet=True
)