import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

NC_URL = os.environ.get("NC_URL")
NC_NAME = os.environ.get("NC_NAME")
NC_PASS = os.environ.get("NC_PASS")
TOKEN = os.environ.get("TOKEN")
BOT_HelloWorld = os.environ.get("BOT_HelloWorld")