import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistake_counter = 0
    print("Welcome to Snowman Meltdown!")

    while True:
        display_word = display_game_state(mistake_counter, secret_word, guessed_letters)

        if '_' not in display_word:
            print('Congratulations! You guessed the word!')
            replay_answer = input("Enter 'R' to replay or 'Q' to quit: ").lower()
            if replay_answer == 'r':
                return play_game()
            elif replay_answer == 'q':
                print("Thank you for playing!")
                return None

        if mistake_counter >= 3:
            print('Game over! The snowman melted!')
            replay_answer = input("Enter 'R' to replay or 'Q' to quit: ").lower()
            if replay_answer == 'r':
                return play_game()
            elif replay_answer == 'q':
                print("Thank you for playing!")
                return None

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter (a-z).")
            elif guess in guessed_letters:
                print("You already guessed this letter. Try another one.")
            else:
                break
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistake_counter += 1

def display_game_state(mistake_counter, secret_word, guessed_letters):
    print(ascii_art.STAGES[mistake_counter])
    display_word = ""
    for char in secret_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    print("Word: " + display_word + '\n')
    return display_word

if __name__ == "__main__":
    play_game()