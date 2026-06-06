def where(words: list, search_word: str):
        if search_word in words:
            print(words.index(search_word))
        else:
            print("Error")


words = [str(input()) for _ in range(5)]
search = str(input())
where(words, search)
