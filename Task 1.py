import random

def choose_word():
    words = ["python", "hangman", "challenge", "programming", "codeAlpha"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n========="
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6
    word_completion = "_" * len(word)

    print("Let's play Hangman!")
    
    while tries > 0 and "_" in word_completion:
        print(display_hangman(tries))
        print(word_completion)
        guess = input("Guess a letter: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
            else:
                print("Incorrect guess.")
                guessed_letters.append(guess)
                tries -= 1
        else:
            print("Invalid input. Please guess a single letter.")
    
    if "_" not in word_completion:
        print("Congratulations! You guessed the word:", word)
    else:
        print(display_hangman(tries))
        print("Sorry, you ran out of tries. The word was:", word)

if __name__ == "__main__":
    hangman()
