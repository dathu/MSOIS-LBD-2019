from gtts import gTTS
#from html.entities import codepoint2name
import os
tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
