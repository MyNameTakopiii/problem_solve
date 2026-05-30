def is_even(num: int):
    return (num & 1) == 0

def main(num: int):

    if is_even(num):
        print("Even")
    else:
        print("Odd")

num1 = int(input())
main(num1)
