from hangman_config import stages,logo2,logo3
from hangman_words import word_list
import random
import os

radom_int = random.randint(1,len(word_list))

choose_word = word_list[radom_int-1]
# print(choose_word)

guess_word = ["_"]*len(choose_word)
# print(guess_word)

# i = os.system("clear")

print(f"{logo3}")
print("\nTo win, guess the word before the person is hung.\n")

guessed_letter = []
remain_life = 5

while remain_life > 0:
    guess_letter = input("Guess a letter:\n").lower()
    i = os.system("clear")
    if guess_letter in guessed_letter:
        print(f"{''.join(guess_word)}")
        print(stages[remain_life])
        print(f"You've already guessed with the letter '{guess_letter}', pick another letter.")
    else:
        guessed_letter.append(guess_letter)

    for index, value in enumerate(choose_word):
        if guess_letter == value:
            guess_word[index] = guess_letter
    
    print(f"{''.join(guess_word)}")

    if "_" not in guess_word:
        remain_life = 0
        print("\nGeninus, genius, genius! You won!")
        print(logo2)
    
    if guess_letter not in choose_word:
        remain_life -= 1

    if remain_life >= 0:
        print(stages[remain_life])
        if guess_letter not in choose_word:
            print(f"'{guess_letter}' is not in the word, you lost 1 life.")

    if remain_life == 0:
        print("The man has been hung, you lose.")
        print(f"\nThe word was '{choose_word}'")

