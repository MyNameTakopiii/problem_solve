def fivex(num: int):

    for i in range(num):
        i += 1
        if i % 5 == 0:
            print('X', end="")
        else:
            print('*', end="")

num1 = int(input())
fivex(num1)