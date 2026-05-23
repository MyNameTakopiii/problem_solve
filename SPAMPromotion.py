def spampro(spam: int):

    price = spam * 100
    count = 0

    if (price >= 2500):
        count += 4
        price -= 200
    elif (price >= 2000):
        count += 1
        price -= 150
    elif (price >= 1000):
        price -= 50

    print(spam + count)
    print(price)

num = int(input())
spampro(num)

