def main(nums):
    total = sum(nums)
    avg = total / len(nums)
    print(f'Sum of these numbers are {total}')
    print(f'Average of these numbers are {avg}')

nums = [int(input()) for _ in range(6)]
main(nums)