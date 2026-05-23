class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# # รับ input แบบ LeetCode
# user_input = input("Input: ")

# # แยก string
# parts = user_input.split(",")
# nums = eval(parts[0].split("=")[1].strip())
# target = int(parts[1].split("=")[1].strip())

# sol = Solution()
# print(sol.twoSum(nums, target))