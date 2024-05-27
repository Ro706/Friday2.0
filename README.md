# Friday: Your Personal Assistant in Python

Friday is a personal assistant application written in Python. It can perform a variety of tasks such as recognizing speech, checking system information, playing games, fetching news, sending emails, telling jokes, and much more. This project integrates various Python libraries and custom modules to provide a comprehensive assistant experience.

## Features

- **Speech Recognition**: Convert speech to text.
- **Text-to-Speech**: Convert text to speech.
- **Password Authentication**: Secure access to the assistant.
- **System Monitoring**: Check CPU and RAM usage.
- **Weather Updates**: Get current weather information.
- **Schedule Management**: Retrieve daily schedules from a MySQL database.
- **Web Browsing**: Open various websites like YouTube, Google, Stack Overflow, and GitHub.
- **Games**: Play tic-tac-toe and ghost game.
- **Email**: Send emails.
- **Jokes**: Tell jokes.
- **Wikipedia**: Search and retrieve information from Wikipedia.
- **News**: Get the latest news.
- **Photo Capture**: Take photos using the system camera.

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
