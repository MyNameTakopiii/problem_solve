def uporlow(word: str):

    if word.islower():
        return "Lower"
    elif word.isupper():
        return "Upper"
    else:
        return "Mixed"

print(uporlow(str(input())))