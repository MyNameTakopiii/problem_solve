def calc_power(base, expo):
    if expo <= 1:
        return base
    return base * calc_power(base, expo - 1)

result = calc_power(int(input()), int(input()))
print(result)