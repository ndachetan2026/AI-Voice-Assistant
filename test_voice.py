import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

print("Available Voices:")
for i, voice in enumerate(voices):
    print(i, voice.name)

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

engine.say("This is the first test.")
engine.runAndWait()

engine.say("This is the second test.")
engine.runAndWait()

engine.say("This is the third test.")
engine.runAndWait()