def shout(word: str, count: int):

    for _ in range(count):
        final = word * count

    print(f'{final}!!!')


shout(str(input()), int(input()))