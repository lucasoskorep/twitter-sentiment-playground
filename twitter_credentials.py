# Variables that contains the user credentials to access Twitter API
import os

from dotenv import load_dotenv

load_dotenv()


ACCESS_TOKEN = os.getenv('ATOKEN', '0')
ACCESS_TOKEN_SECRET = os.getenv('ASECRET', '0')
CONSUMER_KEY = os.getenv('APIKEY', '0')
CONSUMER_SECRET = os.getenv('APISECRET', '0')
