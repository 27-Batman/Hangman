# Hangman in Python
from wordlist import words
import random

# Dictionary for hangman ASCII art
hangman_art = {
    0: ("     ", "     ", "     "),
    1: ("  o  ", "     ", "     "),
    2: ("  o  ", "  |  ", "     "),
    3: ("  o  ", " /|  ", "     "),
    4: ("  o  ", " /|\\ ", "     "),
    5: ("  o  ", " /|\\ ", " /   "),
    6: ("  o  ", " /|\\ ", " / \\ ")
}

def display_man(wrong_guesses):
    """Displays the hangman figure based on wrong guesses."""
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_word(word):
    """Displays the word with spaces between characters."""
    print("Word: " + " ".join(word))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    hint_text = f"Hint: The word refers to a living creature that starts with '{answer[0].upper()}' and ends with '{answer[-1].upper()}'."

    print("Welcome to Hangman! Try to guess the word.")
    print(hint_text)

    while True:
        display_man(wrong_guesses)
        display_word(hint)
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_word(answer)
            print("\n🎉 YOU WIN! 🎉")
            break
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_word(answer)
            print("\n💀 YOU LOSE! The word was:", "".join(answer))
            break

    print("\nThank you for playing!")

if __name__ == '__main__':
    main()
