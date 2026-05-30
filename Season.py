def Season(month: int, day: int):
    if (month, day) >= (12, 21) or (month, day) < (3, 21):
        return "Winter"
    elif (month, day) < (6, 21):
        return "Spring"
    elif (month, day) < (9, 21):
        return "Summer"
    else:
        return "Fall"

month = int(input())
day = int(input())
print(Season(month, day))