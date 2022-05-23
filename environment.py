import os

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
STRING_SESSION = os.environ.get("STRING_SESSION", None)
DEFAULTUSERBIO = os.environ.get("DEFAULTUSERBIO", None)
OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
