from cryptography.fernet import Fernet
import google.generativeai as palm
import pyttsx3
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    # Function to speak text
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.say(text)
    engine.runAndWait()
def chat(quary,key):
        password = b'gAAAAABmEo5WQYsnjRvqreGKbEe6iEz3KYlQ3nFX5wv8ZQDcDDkeknAnxrLkICxV1qcdCZIwDzLS07liWICvHezvJrTex5s0gRtknIfyNgWgtcPds1WNSBbVlF-tf1M7CNJ9YHdteRsL'
        f_obj = Fernet(key)
        dec_key = f_obj.decrypt(password).decode()
        API_KEY = dec_key
        palm.configure(api_key = API_KEY)
        prompt = quary
        response=palm.chat(messages=prompt,temperature=0.2,context="Speak like a AI assistant")
        count = 0
        for message in response.messages:
            for i in message['content'].split('\n'):
                    if count != 0:
                        print(i)
                        speak(i)
                    count += 1
