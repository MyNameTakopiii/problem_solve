def count_n(n: int, count = 1):
    print(count)

    if n != count:
        count_n(n, count + 1)

count_n(int(input()))