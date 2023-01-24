import random
names_str = input("Give me everybody's names, seperated by a comma.\n")
names = names_str.split(",")

random_choice = random.randint(0, len(names) - 1 )
person_choice = names[random_choice]
print(f"{person_choice} is going to buy the meal.")