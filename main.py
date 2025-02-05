# Hangman in python
import random


#dictionary of key
hangman_art = {0: ("     ",
                   "     ",
                   "     "),
               1: ("  o  ",
                   "     ",
                   "     "),
               2: ("  o  ",
                   "  |  ",
                   "     "),
               3: ("  o  ",
                   " /|  ",
                   "     "),
               4: ("  o  ",
                   " /|\\ ",
                   "     "),
               5: ("  o  ",
                   " /|\\ ",
                   " /   "),
               6: ("  o  ",
                   " /|\\ ",
                   " /|\\ ")}

for line in hangman_art[6]:
    print(line)