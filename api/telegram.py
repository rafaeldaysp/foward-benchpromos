import requests
import os

token, chatId = (os.getenv('TELEGRAM_BOT_TOKEN'), os.getenv('TELEGRAM_CHAT_ID'))
baseUrl = f'https://api.telegram.org/bot{token}'

def sendPhoto(imageUrl: str, caption: str) -> None:
  requests.post(f'{baseUrl}/sendPhoto', data={
    "photo": imageUrl,
    "caption": caption,
    "chat_id": chatId
  }) 