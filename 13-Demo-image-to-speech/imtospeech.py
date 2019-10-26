from PIL import Image
from gtts import gTTS

import pytesseract
import vlc

im = Image.open("image.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')
print(text)


tts = gTTS(text)

tts.save("t1.mp3")

player = vlc.MediaPlayer("/home/pi/Desktop/t1.mp3")

player.play()
