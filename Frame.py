def frame(word: str):
    for _ in range(len(word) + 2):
        print('*', end='')
    print(f'\n|{word}|')
    for _ in range(len(word) + 2):
        print('*', end='')

word = str(input())
frame(word)