import random

def guess_number():
    print("Welcome to the number Guessing Game!")

    print("I'm thinking of a number between 1 and 100, try to guess it")
    number = random.randint(1,100)
    print(number)

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    def diffcult_level(difficulty):
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5

    chance = diffcult_level(difficulty)

    def guess(attempt,number):
        if attempt == number:
            print(f"Correct! The answer was {attempt}. Thanks for completing that! 😁")
        elif attempt > number:
            print("Too high.")
            print("Guess again.")
        elif attempt < number:
            print("Too low.")
            print("Guess again.")

    run = True
    while run:
        if chance == 0:
            run = False
        else:
            attempt = int(input("Make a guess: "))
            guess(attempt,number)
            if attempt == number:
                run = False
            else:
                chance -= 1
                if chance > 0:
                    print(f"Your have {chance} attempts remaining to guess the number")
                else:
                    print(f"Your have no attempts remaining to guess the number, you lose.")


    play_again = input("\nDo you want to play again? Type 'y' if yes and 'n' to quit.")
    if play_again == 'y':
        guess_number()
    else:
        print("Goodbye.")

guess_number()
        



# run = True
# while run:

# attempt = int(input("Take you guess: "))

# print(f"You have {guesses} guesses left for the number that I'm thinking of.")

# print(f"Last try to guess the number that I'm thinking of.")

# print(f"Correct! The answer was {guess_this}. Thanks for completing that! 😁")

# print("Game over.")

# print("Too low.")

# print("Too high.")


# play_again = input("\nDo you want to play again? Type 'y' if yes and 'n' to quit.")
# if play_again == 'y':
# clear()
# guess_the_number()
# else:
# print("Goodbye.")