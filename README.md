# Friday: Your Personal Assistant in Python

Friday is a personal assistant application written in Python. It can perform a variety of tasks such as recognizing speech, checking system information, playing games, fetching news, sending emails, telling jokes, and much more. This project integrates various Python libraries and custom modules to provide a comprehensive assistant experience.
---
## Features
### 1. **Speech Recognition**
- **Functionality**: Converts spoken words into text.
- **Implementation**: Uses the `speech_recognition` library to capture audio from the microphone and recognize speech using Google's speech recognition API.

### 2. **Text-to-Speech**
- **Functionality**: Converts text into spoken words.
- **Implementation**: Uses the `pyttsx3` library to convert text to speech, allowing Friday to communicate with the user.

### 3. **Password Authentication**
- **Functionality**: Ensures secure access to the assistant.
- **Implementation**: Prompts the user for a password, which is encrypted and verified using the `cryptography` library and custom security methods.

### 4. **System Monitoring**
- **Functionality**: Checks and reports CPU and RAM usage.
- **Implementation**: Uses the `psutil` library to retrieve and display detailed information about the system's CPU and RAM usage.

### 5. **Weather Updates**
- **Functionality**: Provides current weather information.
- **Implementation**: Fetches weather data from an API (such as OpenWeatherMap) and reports it to the user. This requires an API key and an internet connection.

### 6. **Schedule Management**
- **Functionality**: Retrieves daily schedules from a MySQL database.
- **Implementation**: Connects to a MySQL database using the `pymysql` library to fetch and display the user's schedule for the current day.

### 7. **Web Browsing**
- **Functionality**: Opens various websites like YouTube, Google, Stack Overflow, and GitHub.
- **Implementation**: Uses the `webbrowser` library to open URLs in the default web browser.

### 8. **Games**
- **Functionality**: Offers a selection of games to play, such as tic-tac-toe and ghost game.
- **Implementation**: Integrates custom game modules (`game1` and `game2`) and opens a web-based number game using the `webbrowser` library.

### 9. **Email**
- **Functionality**: Sends emails to specified recipients.
- **Implementation**: Uses a custom module (`core.mail`) to handle email composition and sending, requiring the user's input for email content and recipient address.

### 10. **Jokes**
- **Functionality**: Tells random jokes.
- **Implementation**: Uses the `pyjokes` library to fetch and read out a random joke.

### 11. **Wikipedia**
- **Functionality**: Searches Wikipedia and retrieves summaries.
- **Implementation**: Uses the `wikipedia` library to search for a query and fetch a brief summary of the topic.

### 12. **News**
- **Functionality**: Provides the latest news updates.
- **Implementation**: Uses a custom module (`core.news`) to fetch and report news from a news API. This requires an API key and an internet connection.

### 13. **Photo Capture**
- **Functionality**: Takes photos using the system's camera.
- **Implementation**: Uses a custom module (`core.PhotoCaptureApp`) to create a graphical interface for capturing photos.

### 14. **Time and Date**
- **Functionality**: Provides the current time and date.
- **Implementation**: Uses the `time` module to get and report the current time and date.

### 15. **Greeting**
- **Functionality**: Greets the user based on the time of day.
- **Implementation**: Uses a custom module (`core.wishme`) to determine the appropriate greeting and speaks it to the user.

### 16. **Chat with Bard**
- **Functionality**: Engages in a conversation with the user using the Bard API.
- **Implementation**: Uses a custom module (`core.bard`) to handle chat interactions, providing responses to user queries.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ro706/Friday2.0
   cd Friday2.0
   ```

2. **Install Dependencies**:
   Install the required Python libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MySQL Database**:
   Create a MySQL database and table to store the schedule information. Update the database connection details in the `get_schedule` function.

4. **Set Up API Keys**:
   Obtain API keys for the weather and news services and update the respective modules.

## Usage

Run the main script to start the assistant:
```bash
python main.py
```

## Modules

### Core Modules

- **core.bard**: Handles chat functionalities with the Bard API.
- **core.mail**: Manages email sending functionalities.
- **core.PhotoCaptureApp**: Provides functionalities for capturing photos.
- **core.security.secure**: Manages password encryption and validation.
- **core.news**: Fetches and reports the latest news.
- **core.wishme**: Greets the user based on the time of the day.
- **core.weather**: Provides weather updates.

### Game Modules

- **game.game1**: Tic-tac-toe game.
- **game.game2**: Ghost game.

### Other Libraries

- **pymysql**: Interface with MySQL database.
- **speech_recognition**: Recognize speech using various APIs.
- **pyttsx3**: Text-to-speech conversion.
- **psutil**: Retrieve system information.
- **pyjokes**: Retrieve random jokes.
- **wikipedia**: Retrieve information from Wikipedia.
- **webbrowser**: Open URLs in a web browser.
- **cryptography**: Encrypt and decrypt passwords.

## Custom Functions and Classes

### Functions

- **speak(text)**: Converts text to speech.
- **get_schedule(day)**: Retrieves the schedule for a given day from the MySQL database.
- **handle_interrupt(sig, frame)**: Gracefully exits the program on Ctrl+C press.

### Classes

- **RecognizeSpeech**: Manages speech recognition functionalities.
- **Password**: Handles password encryption and validation.
- **Ram**: Retrieves and displays RAM usage information.
- **Cpu**: Retrieves and displays CPU usage information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the developers of the libraries and APIs used in this project.

## Contact

For any inquiries or feedback, please contact [Ro706](https://github.com/Ro706).

---

**Note**: Ensure you have all the required dependencies installed and properly configured to use all features of Friday. Modify the code as needed to suit your specific requirements.
