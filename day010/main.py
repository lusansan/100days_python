from material import logo


def cal():
    print(logo)
    num_1 = int(input("What is the first number?\n"))
    run = True 
    while run:
        print("+\n-\n*\n/")
        operation = input("Pick on operation:\n") 
        num_2 = int(input("What is the next number?\n"))
        ret = eval(str(num_1) + operation + str(num_2))

        print(f"Type 'y' to continue calculating with {ret}, type 'n' to exit or type 'new' for a brand new calculation")
        continue_calc = input("Type y/n/new: ").lower()
        if continue_calc == 'y':
            run = True
            num_1 = ret
        elif continue_calc == 'new':
            cal()
        elif continue_calc == 'n':
            run = False
            print("\nGoodbye.")
        else:
            print("Invalid response.")
            run = False
            print("\nGoodbye.")
cal()

