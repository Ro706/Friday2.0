import pymysql
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
import core.PhotoCaptureApp as photo
from cryptography.fernet import Fernet
import core.security.secure as secure
import core.news as news
import core.wishme as wish
import core.weather as weather
import game.game1 as game1
import game.game2 as game2
from datetime import datetime
import signal
from typing import List, Tuple

def handle_interrupt(sig, frame):
    """Gracefully exits the program on Ctrl+C press."""
    print("exiting...")
    exit(0)

signal.signal(signal.SIGINT, handle_interrupt)  # Register the signal handler

# Initializing text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

# Function to speak text
def speak(text):
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

        # Trying to recognize the speech
        try:
            print("Recognizing...")
            query = self.r.recognize_google(audio, language='en-in')
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query.lower()

# Password class for checking password
class Password:
    def __init__(self, password):
        self.password = password

    def check(self):
        key = secure.getdata()
        f_obj = Fernet(key)
        enc_message = f_obj.encrypt(self.password.encode())
        return secure.checkdata(enc_message, self.password)

# RAM class for checking RAM information
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
        # Get the swap memory details (if exists)
        system = psutil.virtual_memory()
        print(f'Total :{self.get_size(system.total)} ')
        print(f'Available :{self.get_size(system.available)}')
        print(f'Used :{self.get_size(system.used)}')
        print(f'Percentage :{system.percent}%')
        swap = psutil.swap_memory()
        print('\nSwap partition:')
        print(f'Total: {self.get_size(swap.total)}')
        print(f'Free: {self.get_size(swap.free)}')
        print(f'Used: {self.get_size(swap.used)}')
        print(f'Percentage: {swap.percent}%')

# CPU class for checking CPU information
class Cpu:
    def __init__(self):
        self.cpu_percent = psutil.cpu_percent(interval=1)
        self.cpu_freq = psutil.cpu_freq()
        self.cpu_count = psutil.cpu_count()
        self.cpu_time = psutil.cpu_times()

    def print_detail(self):
        print('cpu_percent: ', self.cpu_percent)
        time.sleep(0.9)
        print('cpu_freq: ', self.cpu_freq)
        time.sleep(0.9)
        print('cpu_count: ', self.cpu_count)
        time.sleep(0.9)
        print('cpu_times: ', self.cpu_time)
        time.sleep(0.9)

# Function to get schedule from the database
def get_schedule(day: str) -> List[Tuple[str, str]]:
    try:
        # Connect to the MySQL database
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root123',
            database='friday'
        )
        cursor = conn.cursor()

        # Extract the day name from the datetime object
        day_name = day.strftime("%A")

        # Query to fetch the schedule for the given day
        query = "SELECT time, subject FROM timetable_a_sem1 WHERE day = %s"
        cursor.execute(query, (day_name,))

        # Fetch all results
        schedule = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return schedule

    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return []

def get_schedule_by_time(time: str) -> List[Tuple[str, str]]:
    try:
        # Connect to the MySQL database
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root123',
            database='friday'
        )
        cursor = conn.cursor()

        # Query to fetch the schedule for the given time
        query = "SELECT day, subject FROM timetable_a_sem1 WHERE time = %s"
        cursor.execute(query, (time,))
        if cursor.rowcount == 0:
            speak("free time boss")
        # Fetch all results
        schedule = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return schedule

    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return []
# Main class for the main program
if __name__ == "__main__":
    wish.wishme()
    # Friday introduction
    speak("Hi, I am Friday. Can you please tell me your password?")
    obj = RecognizeSpeech()  # Object of RecognizeSpeech class
    while True:
        # Password checking section
        password_input = getpass.getpass("Password: ")
        check_password = secure.password_is_correct(password_input)
        if not check_password:
            # Checking password if match then break else ask again
            speak("Wrong password. Please try again.")
        else:
            break
    while True:
        # Listening section for commands or prompts
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
            exit(0)  # Exiting the program
        elif "weather" in query:
            # Weather section: printing weather of Nagpur city
            weather.tellmeTodaysWeather()
        elif "date" in query:
            # Date section: printing today's date in dd-mm-yyyy format
            date = time.strftime("%d %m %Y")
            print(date)  # Printing date
            speak(f"Today's date is {date}")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")  # Opening YouTube in web browser
        elif "open google" in query:
            webbrowser.open("google.com")  # Opening Google in web browser
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")  # Opening Stack Overflow in web browser
        elif "open github" in query:
            webbrowser.open("github.com")  # Opening GitHub in web browser
        elif "game" in query:
            # Game section: playing games
            # Game 1: tic tac toe
            # Game 2: ghost game
            # Game 3: play with number web game
            speak("Which game do you want to play")
            speak("tic tac toe ")
            print("tic tac toe: game1")
            speak("or")
            speak("Ghost Game")
            print("Ghost Game: game2")
            speak("or")
            speak("play with number web game")
            print("play with number: game 3")
            speak("select game")
            print("select game: game1 or game2 or game3")
            game = str(input("Enter game: "))
            if "game1" in game or "tic tac toe" in game:
                game1.game1()
            elif "game2" in game or "ghost game" in game:
                game2.game2()
            elif "game3" in game or "play with number" in game:
                webbrowser.open("https://ro706.github.io/play-with-number/")
            else:
                speak("Sorry, I didn't get that. Can you please repeat?")
        elif "time" in query:
            time_now = time.strftime("%I:%M %p")  # Time format 24 hours
            speak(time_now)
        elif "hello" in query:
            wish.wishme()  # Calling wishme function
        elif "spotify" in query:
            os.system("spotify")  # Opening Spotify app in system: For that you need to install Spotify application
        elif "notepad" in query:
            os.system("notepad")  # Opening Notepad app in system: For that you need to install Notepad application
        elif "news" in query:
            news.news_report()  # Calling news_report function from news.py file in core folder
        elif "ram" in query:
            # RAM section: calculating RAM usage
            speak("Calculating RAM usage")
            ram_instance = Ram()  # Creating an instance of the Ram class
            ram_instance.ram_info()
        elif "cpu" in query:
            # CPU section: calculating CPU usage
            speak("Calculating CPU usage")
            cpu_instance = Cpu()  # Creating an instance of the Cpu class
            cpu_instance.print_detail()
        elif "wikipedia" in query:
            # Wikipedia section: searching Wikipedia
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                print(e)
        elif "mail" in query:
            # Mail section: sending email
            try:
                speak("What should I say?")
                content = obj.listen()  # Listening content to send
                speak("Whom should I send?")
                to = input("Enter receiver's email address: ")
                mail.sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        elif "photo" in query:
            # Photo section: taking photo
            photo.create_gui()
        elif "joke" in query:
            # Jokes section: telling jokes
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif "complete schedule" in query:
            # Schedule section: fetching schedule from the database
            today = datetime.today()
            schedule = get_schedule(today)
            print(f"Schedule for {today.strftime('%A')}:")
            for time, subject in schedule:
                print(f"Time: {time}, Subject: {subject}")
                speak(f"Time: {time}, Subject: {subject}")
        elif "schedule" in query:
            time = query.split(" ")[-1]
            schedule = get_schedule_by_time(time)
            if schedule:
                print(f"Schedule for {time}:")
                for day, subject in schedule:
                    print(f"Day: {day}, Subject: {subject}")
                    speak(f"Day: {day}, Subject: {subject}")
            else:
                print("Sorry, I couldn't find any schedule for that time.")
                speak("Sorry, I couldn't find any schedule for that time.")
        else:
            speak("Hmmm.....")
            if query != 'None':
                bard.chat(query, secure.bardapi())
            else:
                continue
            
# End of the program
# Thank you!
# Friday: Your Personal Assistant in Python
# https://github.com/Ro706/Friday2.0
