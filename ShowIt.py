word_list = []

amount = int(input())

for _ in range(amount):
    words = str(input())
    word_list.append(words)

for _ in range(amount):
    print(word_list.pop())


