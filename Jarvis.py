import datetime

print("🤖 JARVIS Mobile Edition")
print("Type your command. Type 'exit' to stop.")

while True:
    command = input("You: ").lower().strip()

    if command == "exit":
        print("JARVIS: Goodbye!")
        break

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("JARVIS:", time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        print("JARVIS:", date)

    elif "hello" in command or "hi" in command:
        print("JARVIS: Hello! How can I help you?")

    else:
        print("JARVIS: I don't understand that command yet.")