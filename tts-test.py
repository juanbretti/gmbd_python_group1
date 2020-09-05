# %%
# https://pypi.org/project/pyttsx3/

import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.say('My current speaking rate is ' + str(rate) + ', this is a demo using TTS. Please consider saying Juan Pedro.')
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World', 'test.mp3')
engine.runAndWait()

# %%
# https://pypi.org/project/gTTS/

from gtts import gTTS
import os 

tts = gTTS('My current speaking rate is, this is a demo using TTS. Please consider saying Juan Pedro.')
tts.save('hello.mp3')

os.system("mpg321 hello.mp3") 
# %%
# https://stackoverflow.com/questions/58614450/is-there-a-module-that-allows-me-to-make-python-say-things-as-audio-through-the
# https://stackoverflow.com/questions/1614059/how-to-make-python-speak

import win32com.client as wincl
speaker = wincl.Dispatch("SAPI.SpVoice")
speaker.Speak('My current speaking rate is, this is a demo using TTS. Please consider saying Juan Pedro.')
# %%