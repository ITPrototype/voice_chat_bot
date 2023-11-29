import requests
import json
import os
from dotenv import load_dotenv



load_dotenv()
url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":f'{os.getenv("KEY_VOICE")}'}

payload = {
	"src": "Hello, world!",
	"hl": "en-us",
	"r": "0",
	"c": "mp3",
	"f": "8khz_8bit_mono"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "abad377e15msh48e90b24baceff9p1b6c6cjsn0c701ffac1c6",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

def Get_Audio(text):
  payload['src'] = text
  try:
       response = requests.post(url, data=payload, headers=headers, params=querystring)
       with open("saved.ogg","wb") as audio_file:
            audio_file.write(response.content)
  except json.JSONDecodeError as e:
       print(f'[x] - {e}')

def get_chat_id(token):
    response = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
    data = response.json()
    chat_id = data['result'][0]['message']['chat']['id']
    return chat_id
