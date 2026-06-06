my_list = [1, 3, 7, 41]

def double_it(data: list):
    double = [n*2 for n in my_list]
    return double

print(double_it(my_list))
