import os, pyglet
from gtts import gTTS
from time import sleep
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

def play(texte):
    tts=gTTS(text=texte, lang='fr')
    tts.save("temp.mp3")

    music = pyglet.media.load("temp.mp3", streaming=False)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove("temp.mp3")
