import os, re, time

id_pattern = re.compile(r'^.\d+$')


class Config:
    # Client Config              
    API_ID = int(os.environ.get("API_ID", "23941369")) # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "bbd37235e41a95d03bc144ea6bc7b2cd") # ⚠️ Required       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6609713747:AAH7Ijmim8l-dzaw2fn_0eB8aZgikanVVzc") # ⚠️ Required
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")

    # Database Config 
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority") # ⚠️ Required
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Test")

    # other configs 
    OWNER_ID = int(os.environ.get("OWNER_ID", "6805306768")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) # ⚠️ Required
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002093365834")) # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '') # ⚠️ Required
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    USERDATA = os.environ.get('USERDATA', 'USER_DATA')
    BOT_UPTIME  = time.time()
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None 
    BOT_USERNAME = os.environ.get('BOT_USERNAME', "FZXTest2Bot") # No need if you don't want to auto forward when bot restarted
    SESSION = os.environ.get('SESSION', '') # ⚠️ Required 

    # Web Support 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True)) # for web support on/off
    PORT = os.environ.get("PORT","8080")


