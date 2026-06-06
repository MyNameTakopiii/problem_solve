num_list = []

amount = int(input())

for _ in range(amount):
    nums = int(input())
    num_list.append(nums)

num_list.sort(reverse=True)

for _ in range(amount):
    print(num_list.pop())


