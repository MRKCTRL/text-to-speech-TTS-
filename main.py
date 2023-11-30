import requests
import bs4 BeautifulSoup
from google.cloud import speech
from google.auth import compute_engine
impport json

client = speech.SpeechClient.from_service_account_file('key.json')
end_point = 'https://texttospeech.googleapis.com'


file_name = ''


with open(file_name, 'rb') as f:
    pdf_data = f.read()


audio_file speech.RecongnitionAudio(conent=pdf_data)


config = speech.RecongnitionAudio(
    sample_rate_herts=44100,
    enable_automatic_punction=True,
    langauge='en-US'
)

response = client.recongize(
    config=config,
    audio=audio_file
)
