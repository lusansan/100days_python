import random

words_list_1 = ["ardvark", "baboon", "camel"]

radom_int = random.randint(1,len(words_list_1))

choose_word = words_list_1[radom_int-1]
print(choose_word)

guess_letter = input("Guess a letter.\n").lower()
for i in choose_word:
    if guess_letter == i:
        print("Right")
    else:
        print("Wrong")