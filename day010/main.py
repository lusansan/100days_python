
num_1 = input("What is the first number?\n")

print("+ - * /")

def calculate(num_1,num_2,operation):
    return eval(str(num_1) + operation + str(num_2))

print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation")

continue_calc = input("Type y/n/new: ")

operation = input("Pick on operation:\n") 

num_2 = input("What is the next number?\n")

run = True 

while run:
    
