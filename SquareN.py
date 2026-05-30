def SquareN(num: int):

    for i in range(1, num**2 + 1):
        print(i, end=" ")
        if (i % num == 0):
            print()

num1 = int(input())
SquareN(num1)