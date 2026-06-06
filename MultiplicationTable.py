def multi_table(num: int):

    for i in range(1, 13):
        total = i * num 
        print(f'{num} x {i} = {total}')

multi = int(input())
multi_table(multi)