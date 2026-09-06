import datetime
import subprocess


def speak(text):
    print("JARVIS:", text)
    subprocess.run(["termux-tts-speak", text])


def listen():
    print("\n🎙️ Listening...")
    result = subprocess.run(
        ["termux-speech-to-text"],
        capture_output=True,
        text=True
    )

    command = result.stdout.strip()
    print("You:", command)
    return command.lower()


speak("Hello, I am Jarvis. How can I help you?")

while True:

    command = listen()

    if not command:
        continue

    if command == "exit" or "goodbye" in command:
        speak("Goodbye!")
        break

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {current_date}")

    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    else:
        speak("I don't understand that command yet.")