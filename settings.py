from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.environ.get("DB_NAME")
DB_USER=os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
ALGORITHMS = os.environ.get("ALGORITHMS")
API_AUDIENCE = os.environ.get("API_AUDIENCE")
YOUR_CLIENT_ID = os.environ.get("YOUR_CLIENT_ID")
YOUR_CALLBACK_URI = os.environ.get("YOUR_CALLBACK_URI")
YOUR_CLIENT_SECRET = os.environ.get("YOUR_CLIENT_SECRET")
APP_SECRET_KEY = os.environ.get("APP_SECRET_KEY")
BEARER_TOKEN_FULLACCESS = os.environ.get("BEARER_TOKEN_FULLACCESS")