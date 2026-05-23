def ComparNumber(num_1: int, num_2: int):
    if (num_1 > num_2):
        print(f"{num_1} > {num_2}")
    elif (num_2 > num_1):
         print(f"{num_1} < {num_2}")
    else:
        print(f"{num_1} = {num_2}")

num_1 = int(input())
num_2 = int(input())
ComparNumber(num_1, num_2)