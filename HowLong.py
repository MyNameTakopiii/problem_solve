n = int(input())

if n == 0:
    print(1)
else:
    if n < 0:
        n = -n

    c = 0
    while n > 0:
        n //= 10
        c += 1

    print(c)