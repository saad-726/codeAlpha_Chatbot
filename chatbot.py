import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r"hi|hello", ["Hello!", "Hey there!"]),
    (r"how are you ?", ["I'm doing well, how about you?"]),
    (r"sorry (.*)", ["No problem", "It's okay"]),
    (r"I am fine", ["Great to hear that!", "Awesome!"]),
    (r"what is your name ?", ["You can call me AlphaBot.", "I'm a AlphaBot!"]),
    (r"quit", ["Bye for now!", "Goodbye!"]),
    (r"(.*)", ["I am not sure I understand. Could you elaborate?"])
]

def main():
    print("Hi! I'm a basic ChatBot. Type 'quit' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    main()
