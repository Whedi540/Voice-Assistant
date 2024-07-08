import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech and return the text
def recognize_speech():
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Sorry, my speech service is down."

# Function to speak the given text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to handle voice commands
def handle_command():
    command = recognize_speech()
    output_text.insert(tk.END, f"User: {command}\n")
    response = f"You said: {command}"
    speak_text(response)
    output_text.insert(tk.END, f"Assistant: {response}\n")

# Setting up the GUI
root = tk.Tk()
root.title("Voice-Controlled Personal Assistant")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

# Adding a label
label = tk.Label(root, text="Press the button and speak", bg="#f2f2f2", font=("Arial", 14))
label.pack(pady=10)

# Adding a button to trigger speech recognition
btn_listen = tk.Button(root, text="Listen", command=handle_command, bg="#4CAF50", fg="white", font=("Arial", 12))
btn_listen.pack(pady=20)

# Adding a scrolled text widget to display the conversation
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, font=("Arial", 12))
output_text.pack(pady=10)

# Run the GUI event loop
root.mainloop()