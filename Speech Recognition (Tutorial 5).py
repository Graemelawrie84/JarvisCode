"""This program was developed and written by Graeme.
   This was for an example tutorial for YouTube"""

"""NOTE - you will need a microphone plugged into your computer"""

"""Libraries - for notes on how to install see video 4 in this series"""
import pyttsx3
import speech_recognition as sr #don't forget to 'pip install' this library
import time # this is part of python - you should not need to install this


"""variables"""
r = sr.Recognizer()
keywords = [("jarvis", 1), ("hey jarvis", 1), ] # setting up our 'wake' words
source = sr.Microphone() #setting up which mic we are using


"""Functions"""
def Speak(text):
    rate = 100 #Sets the default rate of speech
    engine = pyttsx3.init() #Initialises the speech engine
    voices = engine.getProperty('voices') #sets the properties for speech
    engine.setProperty('voice', voices[0].id) #Gender and type of voice
    engine.setProperty('rate', rate+50) #Adjusts the rate of speech
    engine.say(text) #tells Python to speak variable 'text'
    engine.runAndWait() #waits for speech to finish and then continues with program
def callback(recognizer, audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords) #Uses Sphinx to recognise speech
        print(speech_as_text) #prints what was said on the screen
        if "jarvis" in speech_as_text or "hey jarvis": #starter names
            Speak("Yes sir?") #Calls 'Speak' and acknowledges user
            recognize_main() #Runs the function recognize_main
    except sr.UnknownValueError: #if there is nothing understood
        print("Oops! Didn't catch that") #prints to screen error message
def start_recognizer(): #initial keyword call
    print("Waiting for a keyword...Jarvis or Hey Jarvis") #Prints to screen
    r.listen_in_background(source, callback) #Sets off recognition sequence
    time.sleep(1000000) #keeps loop running
def recognize_main(): #Main reply call function
    r = sr.Recognizer() # sets r variable
    with sr.Microphone() as source: #sets microphone
        print("Say something!") #prints to screen
        audio = r.listen(source) #sets variable 'audio'
    data = "" #assigns user voice entry to variable 'data'
    try:
        data = r.recognize_google(audio) #now uses Google speech recognition
        data.lower() # makes all voice entries show as lower case
        print("You said: " + data) #shows what user said and what was recognised
#Greetings---------------------------------------------------------------------
        if "how are you" in data: #if statement for specific user speech
            Speak("I am Fine") #calls Speak function and says something
        elif "hello" in data: #elif statement.  Note after first if all statements are else/if or 'elif'
            Speak ("Hi there") #calls Speak function and says something
        else: #what happens if none of the if statements are true
            Speak("I'm sorry sir, I did not understand your request") #calls Speak function and says something
    except sr.UnknownValueError: #whenever you have a try statement you have an exception rule
        print("Jarvis did not understand your request")
    except sr.RequestError as e: # if you get a request error from Google speech engine
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


"""Main program"""
while 1: #This starts a loop so the speech recognition is always listening to you
    start_recognizer() #calls first function 'start_recogniser'


"""Notes
This is a basic speech recognition layout.  In future videos we will enhance this with the ability
to have multiple inputs and outputs, to make the system more reliable nd believable. We will also add some
code to make the system more effective, ignore background noise and make choices from speech
input.  This code will get you started though and show you some basic principles."""
