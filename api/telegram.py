import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

token, chatId = (os.getenv('TELEGRAM_BOT_TOKEN'), os.getenv('TELEGRAM_CHAT_ID'))
baseUrl = f'https://api.telegram.org/bot{token}'

def sendPhoto(imageUrl: str, caption: str, productId: str) -> None:
  res = requests.post(f'{baseUrl}/sendPhoto', data={
    "photo": imageUrl,
    "caption": caption,
    "chat_id": chatId,
    "parse_mode": "Markdown",
    "reply_markup": json.dumps({
      "inline_keyboard": [
      [
        {
          "text": "Postar",
          "callback_data": productId
            
        }
      ]
    ]
      })
  })
  print(res.content)