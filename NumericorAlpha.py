word = str(input()).strip()

if word.isdigit():
    print("Number")

elif word.isalpha():
    print("Alphabet")

elif word.isalnum():
    print("Mixed")

