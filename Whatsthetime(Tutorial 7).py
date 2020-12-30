"""This program was developed and written by Graeme.
   This was for an example tutorial for YouTube
   https://github.com/Graemelawrie84/JarvisCode"""

"""NOTE - you will need a microphone plugged into your computer"""

"""Libraries - for notes on how to install see video 4 in this series"""
import pyttsx3 #text to speech
import speech_recognition as sr #don't forget to 'pip install' this library
import time # this is part of python - you should not need to install this
from openpyxl import * #load workbook in Excel
import random #to allow random replies to questions


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
        #if "hello" in data:
        if data in hello_list:
            hour=datetime.datetime.now().hour
            if hour>=0 and hour<12:
                Speak("Good morning, sir")
            elif hour>=12 and hour<18:
                Speak("Good Afternoon, Sor")
            else:
                Speak("Good Evening, Sir")
            time.sleep(2)
        elif data in how_are_you:
            Speak (random.choice(reply_how_are_you))
            time.sleep(2)
        elif "What is the time" in data:
            strTime=datetime.datetime.now().strftime("%H:%M")
            Speak(f"the time is {strTime}")
            time.sleep(2)
        elif "what day is it" in data:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
                        4: 'Thursday', 5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}
            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                Speak("The day is " + day_of_the_week)
                time.sleep(2)
        else: #what happens if none of the if statements are true
            Speak("I'm sorry sir, I did not understand your request") #calls Speak function and says something
    except sr.UnknownValueError: #whenever you have a try statement you have an exception rule
        print("Jarvis did not understand your request")
    except sr.RequestError as e: # if you get a request error from Google speech engine
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
def excel():
    wb = load_workbook("input.xlsx") #Opens the excel document for data
    wu = wb.get_sheet_by_name('User') #sets the sheet in Excel for user prompts
    wr = wb.get_sheet_by_name('Replies') #sets the sheet in Excel for replies

    global hello_list
    global how_are_you
    urow1 = wu['1'] #hello
    urow2 = wu['2'] #how are you
    hello_list = [urow1[x].value for x in range(len(urow1))]
    how_are_you = [urow2[x].value for x in range(len(urow2))]

    global reply_hello_list
    global reply_how_are_you
    rrow1 = wr['1'] #how are you
    rrow2 = wr['2'] #how are you
    reply_hello_list = [rrow1[x].value for x in range(len(rrow1))]
    reply_how_are_you = [rrow2[x].value for x in range(len(rrow2))]

"""Main program"""
excel()
while 1: #This starts a loop so the speech recognition is always listening to you
    start_recognizer() #calls first function 'start_recogniser'


"""Notes
This program shows a few examples of adding time control to the Jarvis program.
Speak the time, the day and use the time to alter replies."""
