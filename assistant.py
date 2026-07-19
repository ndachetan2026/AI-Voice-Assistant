import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import random

# -------------------- SPEAK FUNCTION --------------------

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -------------------- LISTEN FUNCTION --------------------

def take_command():
    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 1
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=7
)

    try:
        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        ).lower().strip()

        print("You said:", command)
        return command

    except sr.UnknownValueError:
        print("Could not understand.")
        return ""

    except sr.RequestError:
        speak("Please check your internet connection.")
        return ""

    except Exception:
        return ""


# -------------------- START --------------------

speak("Hello Chetan. I am your AI Voice Assistant. How can I help you?")

# -------------------- MAIN LOOP --------------------

while True:

    command = take_command()

    if command == "":
        continue

    # Hello
    if "hello" in command or "hi" in command:
        speak("Hello Chetan. How can I help you?")

    # How are you
    elif any(phrase in command for phrase in [
        "how are you",
        "how are",
        "how r",
        "how r y",
        "how're you",
        "how do you",
        "how you"
    ]):
        speak("I am doing great. Thank you for asking. How are you?")

    # I am fine
    elif any(phrase in command for phrase in [
        "i am fine",
        "i'm fine",
        "fine",
        "doing good",
        "doing great"
    ]):
        speak("I am glad to hear that. Have a wonderful day.")

    # Who are you
    elif "who are you" in command:
        speak("I am your AI Voice Assistant created by Chetan using Python.")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + current_time)

    # Date
    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    # Google
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # YouTube
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
            # ChatGPT
    elif "chat g p t" in command or "chatgpt" in command:
        speak("Opening Chat GPT")
        webbrowser.open("https://chat.openai.com")

    # Calculator
    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    # Notepad
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # Command Prompt
    elif "command prompt" in command or "cmd" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    # VS Code
    elif "vs code" in command or "visual studio code" in command:
        speak("Opening Visual Studio Code")
        os.system("code")

    # Joke
    elif "joke" in command or "tell me a joke" in command:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "Why did the computer go to the doctor? Because it had a virus.",
            "Debugging is like being a detective. Sometimes you are also the criminal.",
            "Why do Java developers wear glasses? Because they don't C sharp."
        ]
        speak(random.choice(jokes))

    # Thank You
    elif "thank you" in command or "thanks" in command:
        speak("You're welcome, Chetan.")

    # Good Morning
    elif "good morning" in command:
        speak("Good morning Chetan. Have a wonderful day.")

    # Good Night
    elif "good night" in command:
        speak("Good night Chetan. Sweet dreams.")

    # Exit
    elif (
        "exit" in command
        or "stop" in command
        or "goodbye" in command
        or "good bye" in command
        or "bye" in command
    ):
        speak("Goodbye Chetan. Have a wonderful day.")
        break

    # Unknown Command
    else:
        speak("Sorry. I don't know that command yet.")