import random
words = ["python", "coding", "laptop", "internet", "keyboard"]
def show_word(word, guessed_letters):
    """Return the word with unguessed letters hidden as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display
def play_hangman():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("=== Welcome to Hangman! ===")
    print("Guess the word one letter at a time.")
    print("You can make", max_wrong, "wrong guesses.\n")

    while wrong_guesses < max_wrong:
        print("Word:", show_word(word, guessed_letters))
        print("Wrong guesses left:", max_wrong - wrong_guesses)
    
        if "_" not in show_word(word, guessed_letters):
            print("\nCongratulations! You guessed the word:", word)
            return

        guess = input("Enter a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed_letters:
            print("You already guessed that letter.\n")
        else:
            guessed_letters.append(guess)
            if guess in word:
                print("Good guess!\n")
            else:
                wrong_guesses += 1
                print("Wrong guess!\n")

    print("Game over! The word was:", word)


play_hangman()