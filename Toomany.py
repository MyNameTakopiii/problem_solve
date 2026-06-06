def too_many(amount: int, find: int):

    num_list = []
    count = 0

    for _ in range(amount):
        nums = int(input())
        num_list.append(nums)
        if find == nums:
            count += 1

    if find in num_list:
        print(count) 
    else:
        print(0)

too_many(int(input()), int(input()))

