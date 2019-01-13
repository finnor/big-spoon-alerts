from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

EMAIL_SERVER  =      os.getenv("EMAIL_SERVER")        or "smtp.gmail.com"
EMAIL_PORT    =  int(os.getenv("EMAIL_PORT"))         or 465
EMAIL_LOGIN   =      os.getenv("EMAIL_LOGIN")         or "username"
EMAIL_PASS    =      os.getenv("EMAIL_PASS")          or "password"
EMAIL_FROM    =      os.getenv("EMAIL_FROM")          or "sender@gmail.com"
EMAIL_TO      =      os.getenv("EMAIL_TO")            or "dump@gmail.com"
EMAIL_NO_DIFF =      os.getenv("EMAIL_NO_DIFF")=="True"

