import speech_recognition as sr
import pyttsx3 
import getpass
import time 
import os
import psutil
import pyjokes
import wikipedia
import webbrowser
import core.bard as bard
import core.mail as mail
from cryptography.fernet import Fernet
import core.security.secure as secure
import core.news as news
import core.wishme as wish 
import core.weather as weather
import game.game1 as game1
import game.game2 as game2
import signal

def handle_interrupt(sig, frame):
    """Gracefully exits the program on Ctrl+C press."""
    print("exiting...")
    exit(0)

signal.signal(signal.SIGINT, handle_interrupt)  # Register the signal handler

# Initializing text-to-speech engine
engine = pyttsx3.init()
engine.energy_threshold = 4000
engine.dynamic_energy_threshold = True
engine.dynamic_energy_adjustment_damping = 0.15
engine.dynamic_energy_ratio = 2.5
# Function to speak text
def speak(text):
    # Function to speak text
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.say(text)
    engine.runAndWait()

# Class to recognize speech
class RecognizeSpeech:
    def __init__(self):
        self.r = sr.Recognizer()
    # Function to listen
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)
        #trying to recognize the speech
        try:
            print("Recognizing...")
            query = self.r.recognize_google(audio, language='en-in')
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query.lower()

# password class for checking password
class Password:
    def __init__(self, password):
        self.password = password

    def check(self):
        key = secure.getdata()
        f_obj = Fernet(key)
        enc_message = f_obj.encrypt(self.password.encode())
        return secure.checkdata(enc_message, self.password)

# ram class for checking ram information
class Ram:
    def __init__(self):
        pass
    def get_size(self, bytes, suffix='B'):
        factor = 1024
        for unit in ['','K','M','G','T','P']:
            if bytes < factor:
                return f'{bytes:.2f}{unit}{suffix}'
            bytes /= factor
    
    def ram_info(self):
        #Get the swap memory details (if exists)
        system = psutil.virtual_memory()
        print(f'Total :{self.get_size(system.total)} ')
        print(f'Available :{self.get_size(system.available)}')
        print(f'Used :{self.get_size(system.used)}')
        print(f'percentage :{system.percent}%')
        swap = psutil.swap_memory()
        print('\nSwap pertition:')
        print(f'Total: {self.get_size(swap.total)}')
        print(f'Free: {self.get_size(swap.free)}')
        print(f'Used: {self.get_size(swap.used)}')
        print(f'Percentage: {swap.percent}%')

# cpu class for checking cpu information
class Cpu:
    def __init__(self):
        self.cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_freq    = psutil.cpu_freq()
        self.cpu_count = psutil.cpu_count()
        self.cpu_time = psutil.cpu_times()
    
    def print_detail(self):
        print('cpu_precent: ', self.cpu_percent)
        time.sleep(0.9)
        print('cpu_freq: ' ,self.cpu_freq)
        time.sleep(0.9)
        print('cpu_count: ' ,self.cpu_count)
        time.sleep(0.9)
        print('cpu_times: ' ,self.cpu_time)
        time.sleep(0.9)     

# main class for main program 
if __name__ == "__main__":
    wish.wishme()
    # friday introduction
    speak("Hi, I am Friday. Can you please tell me your password?")
    obj = RecognizeSpeech() #object of RecognizeSpeech class
    while True:
        # password checking section
        password_input = getpass.getpass("Password: ")
        check_password =  secure.password_is_correct(password_input)
        if not check_password:
            # checking password if match then break else ask again
            speak("Wrong password. Please try again.")
        else:
            break
    while True:
        # listening section for commands or prompts
        query = obj.listen()
        try:  
            speak(query)
            # print('user said: ')
            # print(query) # for debugging
            
        except Exception as e:
            print(e)
            pass
        if "exit" in query:
            print("Bye sir. Have a good day!")
            exit(0) #exiting the program
        elif "weather" in query:
            # weather section : printing weather of nagpur city
            weather.tellmeTodaysWeather()
        elif "date" in query:
            # date section : printing today's date in dd-mm-yyyy format
            date = time.strftime("%d %m %Y")
            print(date) #printng date
            speak(f"Today's date is {date}")
        elif "open youtube" in query:
            webbrowser.open("youtube.com") #opening youtube in web browser 
        elif "open google" in query:
            webbrowser.open("google.com") #opening google in web browser
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com") #opening stackoverflow in web browser
        elif "open github" in query:
            webbrowser.open("github.com") #opening github in web browser
        elif "game" in query:
            # game section : playing games
            # game 1 : tic tac toe
            # game 2 : ghost game
            # game 3 : play with number web game
            speak("which game do you want to play")
            speak("tic tac toe ")
            print("tic tac toe : game1")
            speak("or")
            speak("Ghost Game")
            print("Ghost Game : game2")
            speak("or")
            speak("play with number web game")
            print("play with number : game 3")
            speak("select game")
            print("select game : game1 or game2 or game3")
            game = str(input("Enter game : "))
            if "game1" in game  or "tic tac toe" in game:
                game1.game1()
            elif "game2" in game or "ghost game" in game:
                game2.game2()
            elif "game3" in game or "play with number" in game:
                webbrowser.open("https://ro706.github.io/play-with-number/")
            else:
                speak("Sorry, I didn't get that. Can you please repeat?")
        elif "time" in query:
            time_now = time.strftime("%I:%M %p") #time format 24 hours
            speak(time_now)
        elif "hello" in query:
            wish.wishme() #calling wishme function
        elif "spotify" in query:
            os.system("spotify") #opening spotify app in system : For that you need to install spotify application
        elif "notepad" in query:
            os.system("notepad") #opening notepad app in system : For that you need to install notepad application
        elif "news" in query:
            news.news_report() #calling news_report function from news.py file in core folder
        elif "ram" in query:
            # Ram section : calculating ram usage
            speak("calculating ram usage")
            ram_instance = Ram() # Creating an instance of the Ram class
            ram_instance.ram_info()
        elif "cpu" in query:
            # Cpu section : calculating cpu usage
            speak("calculating cpu usage")
            cpu_instance = Cpu() # Creating an instance of the Cpu class
            cpu_instance.print_detail()
        elif "wikipedia" in query:
            # Wikipedia section : searching wikipedia
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                # if ant error occurs then print error
                print(e)
                speak("Sorry, I didn't get that. Can you please repeat?")
        elif "joke" in query or "jokes" in query:
            a = pyjokes.get_joke()
            # printing jokes 
            print(a)
            speak(a)
        elif "mail" in query:
            # mail section : sending mail
            keywords = secure.getdatamail()
            mail.send_mail(keywords)
        else:
            # updating user if query is not matched
            speak("Hmmm.....")
            if (query != 'None'):
                bard.chat(query,secure.bardapi())
            else:
                speak("Sorry, I didn't get that. Can you please repeat?")