# %%
# https://pypi.org/project/pyttsx3/

import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

"""Saving Voice to a file"""
engine.save_to_file('Clean and develop using Python. This is the presentation from group F. Abdulaziz, Juan Pedro, Jacob, Aleksandar, Esperanza and Addison', 'storage/slide_1.mp3')
engine.save_to_file('EXPLORATORY DATA ANALYSIS, or EDA for short.', 'storage/slide_5.mp3')
engine.save_to_file("DATA PREPARATION. Let's talk about data quality and how to fix.", 'storage/slide_11.mp3')
engine.save_to_file("Modelling. We are going to create and evaluate linear regression models.", 'storage/slide_21.mp3')
engine.save_to_file("Thank you.", 'storage/slide_28.mp3')
engine.runAndWait()

# %%
