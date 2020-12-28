
#Libraries
import pyttsx3
#Functions
def Speak(text):
    rate = 100 #Sets the default rate of speech
    engine = pyttsx3.init() #Initialises the speech engine
    voices = engine.getProperty('voices') #sets the properties for speech
    engine.setProperty('voice', voices[0].id) #Gender and type of voice
    engine.setProperty('rate', rate+50) #Adjusts the rate of speech
    engine.say(text) #tells Python to speak variable 'text'
    engine.runandWait() #runs the previous line and waits for it to complete
#Main program
Speak("Hello World") #calls Speak function and passes text to be said
#Notes
"""
In this chunk of code we call on a function called Speak.  
This code will only work if you have installed PYTTSX3 library.
Use 'Pip Install PYTTSX3' in Command prompt to install library"""
