from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "b081ec8da8cf5263a6593041c1ae2a3b")
      API_ID = int(getenv("API_ID", "21140176"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8480948621:AAElzf6dHKj67E2e_USS_nVc1fLp_jJ3V-8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1003168773809").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
