import yaml
from dotenv import load_dotenv
import os

load_dotenv()

def load_config(path="configs/settings.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

config = load_config()
SECRET_KEY = os.getenv("SECRET_KEY")