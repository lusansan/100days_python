from hangman_config import stages,logo2,logo3
from hangman_words import word_list
import random

words_list_1 = ["ardvark", "baboon", "camel"]

radom_int = random.randint(1,len(words_list_1))

choose_word = words_list_1[radom_int-1]
print(choose_word)

word = input("Guess a letter.\n")

if word in choose_word:
    print("Right")
else:
    print("Wrong")