def starry(word: str):
    star_count = word.count("*")
    noise_count = word.count("#")
    new = word.replace("#", "")
    return f'Star: {star_count}\nNoise: {noise_count}\n{new}'


print(starry(str(input())))


