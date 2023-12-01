import requests
import bs4 BeautifulSoup
from google.cloud import speech
# from google.auth import compute_engine
impport json
# from google.cloud import datastore
# from google.oauth2 import service_account
from google.cloud import texttospeech
froom google.oauth2 import service_account


# end_point = 'https://texttospeech.googleapis.com'
# response = request.get(url=end_point)
# response.raise_for_status()
# data = response.json()


client = texttospeech.TextTpSpeechClient()


credentials = service_account.Credentials.from_service_account_file(
    '/path/to/key.json')

input_text = texttospeech.Synthesis(text=text)

voice = texttospeech.VoiceSelectionParams(
    langauge_code='en-GB',
    name='en-GB-Standard-C',
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
)

audio_config = texttospeech.AudioConfig(
    audio_encodingtexttospeech.AudioEncoding.mp3
)

response = client.synthesize_speech(
    request={'input': input_text, 'voice': voice, 'audio_config':audio_config}
)

with open ('ouutput.mp3', 'wb') as out:
    out.write(response.audio_content)
    print('Audio is ready')
