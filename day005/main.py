import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = input("How many letters would you like in your password?\n")
num_symbols = input(f"How many symbols would you like?\n")
num_numbers = input(f"How many numbers would you like?\n")

if not num_letters.isdigit() or not num_symbols.isdigit() or not num_numbers.isdigit():
    print("Invalid value, enter a number instead.")
else:
    num_letters = int(num_letters)
    num_symbols = int(num_symbols)
    num_numbers = int(num_numbers)

    pw = []
    if num_letters > 0:
        for i in range(0,num_letters):
            pw.append(letters[random.randint(0,len(letters)-1)])
    if num_symbols > 0:
        for i in range(0,num_symbols):
            pw.append(symbols[random.randint(0,len(symbols)-1)])
    if num_numbers > 0:
        for i in range(0,num_numbers):
            pw.append(numbers[random.randint(0,len(numbers)-1)])
    
    pw_str = ''
    for i in range(0,len(pw)):
        j = random.randint(0,len(pw)-1)
        pw_str = pw_str + pw[j]
        del pw[j]


    # random.shuffle(pw)
    # print(f"Here is your password: {''.join(pw)}")

    print(f"Here is your password: {pw_str}")

    if len(pw_str) <= 6:
        print("Your password is weak, try to include at least 8 characters for a stronger password.")
    elif len(pw_str) == 7:
        print("Your password is medium, try to include at least 8 characters for a stronger password.")
    else:
        print("Your password is strong.")