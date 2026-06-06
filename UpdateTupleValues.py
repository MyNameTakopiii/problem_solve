edit = input() # "kiwi"
fruits = ("apple", "banana", "cherry")
fruits_list = list(fruits)
fruits_list[1] = edit
fruits = tuple(fruits_list)
print(fruits) # จะได้ค่า ('apple', 'kiwi', 'cherry')