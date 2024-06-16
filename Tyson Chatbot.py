import re
import tkinter as tk
from tkinter import scrolledtext

# Define some basic rules
rules = {
    r'hi|hello|hey': 'Hello! How can I help you today?',
    r'how are you': 'I am a bot, but I am functioning as expected!',
    r'what is your name': 'I am a Tyson chatbot.',
    r'bye|exit|quit': 'Goodbye! Have a great day!',
    r'help|assist': 'Sure, I am here to help. What do you need assistance with?',
    r'what can you do': 'I can answer simple questions and have basic conversations with you.',
    r'tell me a joke': 'Why don’t scientists trust atoms? Because they make up everything!',
    r'what is ai': 'AI stands for Artificial Intelligence, which refers to the development of computer systems that can perform tasks that typically require human intelligence.',
    r'what is machine learning': 'Machine learning is a subset of AI that involves training algorithms to learn from data and make predictions or decisions without being explicitly programmed.',
    r'are you ai': 'Yes, I am a simple AI-powered chatbot!',
    r'what is your favorite color': 'As an AI, I don\'t have preferences, but I\'ve heard that many people like blue.',
    r'what is the meaning of life': 'The meaning of life is a philosophical question, but some say it\'s to live happily and make a positive impact.',
    r'can you help me with programming': 'Sure, I can try! What specific programming question do you have?',
    r'what is the capital of france': 'The capital of France is Paris.',
    r'who is the president of the united states': 'As of my last update, the President of the United States is Joe Biden.',
    r'what time is it': 'I can\'t tell the time right now, but you can check your device\'s clock!',
    r'how is the weather': 'I can\'t provide real-time weather updates, but you can check a weather website or app!',
    r'tell me something interesting': 'Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!',
    r'what is your purpose': 'My purpose is to assist you with simple questions and provide information to the best of my programmed abilities.'
}

def respond(user_input):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm not sure how to respond to that."

def send_message():
    user_input = user_input_entry.get()
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    response = respond(user_input)
    chat_log.insert(tk.END, "Chatbot: " + response + "\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    user_input_entry.delete(0, tk.END)

# Set up the main application window
root = tk.Tk()
root.title("Chatbot")

# Create a chat log window
chat_log = scrolledtext.ScrolledText(root, state='disabled', wrap=tk.WORD)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry box for user input
user_input_entry = tk.Entry(root, width=80)
user_input_entry.pack(padx=10, pady=10, fill=tk.X, expand=True)
user_input_entry.bind("<Return>", lambda event: send_message())

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10)

# Start the main event loop
root.mainloop()
