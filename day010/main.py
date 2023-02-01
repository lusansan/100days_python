
num_1 = input("What is the first number?\n")

print("+\n-\n*\n/")

def calculate(num_1,num_2,operation):
    return eval(str(num_1) + operation + str(num_2))

print(f"Type 'y' to continue calculating with {answer}, type 'n' to exit or type 'new' for a brand new calculation")

continue_calc = input("Type y/n/new: ")

operation = input("Pick on operation:\n") 

num_2 = input("What is the next number?\n")



def cal():
    run = True 
    while run:
        num_1 = input("What is the first number?\n")
        print("+\n-\n*\n/")
        operation = input("Pick on operation:\n") 
        num_2 = input("What is the next number?\n")
        ret = calculate(num_1, num_2, operation)

        print(f"Type 'y' to continue calculating with {ret}, type 'n' to exit or type 'new' for a brand new calculation")
        continue_calc = input("Type y/n/new: ").lower()
        if continue_calc == 'y':
            num_2 = input("What is the next number?\n")
            print("+\n-\n*\n/")
            operation = input("Pick on operation:\n") 
            ret = calculate(num_1, num_2, operation)
            print(f"Type 'y' to continue calculating with {ret}, type 'n' to exit or type 'new' for a brand new calculation")
        elif continue_calc == 'new':
            cal()
        elif continue_calc == 'n':
            run = False
        else:
            print


