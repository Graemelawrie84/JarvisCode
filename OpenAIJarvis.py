import openai
import speech_recognition as sr
import pyttsx3

# Set up OpenAI API key
openai.api_key = 'Put your API here'

# Text-to-speech setup
tts_engine = pyttsx3.init()

def text_to_speech(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Speech recognition setup
recognizer = sr.Recognizer()

def listen_for_voice():
    with sr.Microphone() as source:
        print("Jarvis: Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio).strip()
        print(f"You: {user_input}")
        return user_input
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"Error: {str(e)}"

def chat_with_gpt3(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
        )
        reply = response['choices'][0]['text'].strip()
        return reply
    except Exception as e:
        return str(e)

print("Jarvis: Hello! How can I assist you today?")
while True:
    user_input = listen_for_voice()
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Jarvis: Goodbye!")
        break

    conversation_history = f"You: {user_input}\nJarvis:"
    response = chat_with_gpt3(conversation_history)
    print(f"Jarvis: {response}")
    text_to_speech(response)
