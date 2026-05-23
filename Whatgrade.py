def whatgrade(score: int):
    if (100 >= score and score >= 80):
        return print("A")
    elif (80 > score and score >= 75):
        return print("B+")
    elif (75 > score and score >= 65):
        return print("B")
    elif (65 > score and score >= 70):
        return print("C+")
    elif (65 > score and score >= 60):
        return print("C")
    elif (60 > score and score >= 55):
        return print("D+")
    elif (55 > score and score >= 50):
        return print("D")
    elif (50 > score and score >= 0):
        return print("F")
    else:
        print("Error")

num = int(input())
whatgrade(num)