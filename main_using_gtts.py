from gtts import gTTS

langauge = 'en'
text = with open(file_name, <pdf.file>) as f:
        pdf_data = f.read()

speech = gTTS(text=text, lang=langauge, slow=False, tlds='com.au')
speech.save(speech.mp3)
.gitignore
