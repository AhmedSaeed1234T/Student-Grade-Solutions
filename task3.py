import random

def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return ''.join(scrambled)

def word_scramble_game():
    words = ["DataStructue", "OOP", "Database", "algorithm"]
    original_word = random.choice(words)
    scrambled_word = scramble_word(original_word)

    print("Welcome to the Word Scramble Game!\n")
    print(f"The scrambled word is: {scrambled_word}\n")
    
    attempts = 5
    while attempts > 0:
        guess = input("Guess the original word: ").strip()

        if not guess:
            print("Please enter a valid word.\n")
            continue

        if guess == original_word:
            print("\nCongratulations! You guessed the word correctly!\n")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess. You have {attempts} attempts left.\n")
            else:
                print("\nSorry, you've run out of attempts.")
                print(f"The original word was: {original_word}\n")

if __name__ == "__main__":
    word_scramble_game()
