from math import ceil
def print_calc(height, width, cover):
    print("You'll need {} cans of paint.".format(ceil(test_h*test_w/coverage)))

test_h = int(input("Height of wall:\n"))
test_w = int(input("Width of wall:\n"))
coverage = 5
print_calc(height = test_h, width = test_w, cover = coverage)