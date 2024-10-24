from random import *
length = 6
words = input("How many words? ")

def randStr(length):
    """Returns a string of given length composed of
    a set of random characters."""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word = ""
    for i in range(int(length)):
        word += alphabet[randint(0, len(alphabet) - 1)]
    return word

def makeWord(num_of_words):
    """Generates random words and writes them to a file."""
    with open("random_words.txt", "w") as f:
        for i in range(int(num_of_words)):
            store = randStr(6)
            f.write(store + "\n")

makeWord(words)
