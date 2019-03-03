import random

def print_matrix():
    n = int(input("enter a number that will determine the size of matrix: "))

    for i in range(0,n):
        strin = str(random.randint(0, 1))
        for q in range(0,n-1):
            strin+=" " + str(random.randint(0, 1))
        print(strin)
