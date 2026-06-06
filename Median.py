def median(amount: int):
    num_list = []

    for _ in range(amount):
        number = float(input())
        num_list.append(number)
    
    num_list.sort()

    n = len(num_list)
    mid = n // 2
    
    if n % 2 == 1:
        print(num_list[mid])
    else:
        left = num_list[mid - 1]
        right = num_list[mid]
        print((left + right) / 2)


amount = int(input())
median(amount)




