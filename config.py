import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 26416722))

    API_HASH = os.environ.get("API_HASH", "e4fccf54d5e406dc453160b8f90311f2")
