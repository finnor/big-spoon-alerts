import settings
from big_spoon_alerts.scraper import Scraper
from big_spoon_alerts.message import Message
from big_spoon_alerts.mail import sendEmail
from big_spoon_alerts.differ import diff
import json

# get past menu
try:
    menu_file = open('storage/menu.json','r')
    previous_menu = json.loads(menu_file.read())
    menu_file.close()
except IOError:
    previous_menu = []

# get current menu
current_menu = Scraper.scrape()

if(current_menu!=None and len(current_menu)>0):
    menu_diff = diff(current_menu, previous_menu)

    if(settings.EMAIL_NO_DIFF or len(menu_diff["dropped"])>0 or len(menu_diff["new"])>0):
        message = Message(menu_diff, current_menu)
        sendEmail(emailFrom    = settings.EMAIL_FROM,
                  emailTo      = settings.EMAIL_TO.split(';'),
                  subject      = message.getSubject(),
                  body         = message.getBody(),
                  login        = settings.EMAIL_LOGIN,
                  password     = settings.EMAIL_PASS,
                  smtpServer   = settings.EMAIL_SERVER,
                  smtpPort     = settings.EMAIL_PORT)

    menu_file = open('storage/menu.json', 'w')
    json.dump(current_menu, menu_file)
    menu_file.close()
else:
    print("Failed to retrieve current menu")
