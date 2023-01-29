def prime_checker(number):
    if number < 2:
        print("Please input a number above 1.")
    # elif number == 2 :
    #     print(f"{number} is a prime number.")
    else:
        is_prime = True
        for i in range(2,number//2+2):
            if n % i == 0 and i < number:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")


n = int(input("Check this number:\n"))
prime_checker(number = n)

# for n in range(2,50):
#     prime_checker(number = n)