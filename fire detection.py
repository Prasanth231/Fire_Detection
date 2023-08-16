################################################################################
import cv2
import telegram
from telethon import TelegramClient, events, functions, types
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import geocoder
################################################################################
fire_cascade = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture(0)
min_size = (230, 230)
confidence_threshold = 30
################################################################################
#ID to connect Telegram bot
api_id = 1234567 
api_hash = "f183ce9********6accc6b6ad53db"
bot_token = "1797608524:A***********7NunlH7ThH8ZGLAM"
bot_user_name = "@Msgchecka2z_bot"
chat_id = 123456789
URL = "https://web.telegram.org/#/im?p=@Msgchecka2z_bot"
phone = +91987543214
session_file = "@*****8"
password = ""  
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)
client = TelegramClient(session_file, api_id, api_hash)
fire=0
################################################################################
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    fires = fire_cascade.detectMultiScale(gray, 1.3, 5, minSize=min_size)
    for (x, y, w, h) in fires:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        if w * h > confidence_threshold:
            g=geocoder.ip('me')
            location = g.latlng
            msg= f"Fire Detected at Here location at Latitude: {location[0]}, Longitude: {location[1]} come quickly"
            bot.sendMessage(chat_id,msg)
    cv2.imshow('Fire Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
