from gtts import gTTS
import vlc
tts = gTTS(text='Good morning', lang='en')

tts.save("good.mp3")

player = vlc.MediaPlayer("/home/pi/Desktop/good.mp3")

player.play()

