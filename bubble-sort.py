""" Bubble Sort in Python """
nums = input("Enter the numbers, separated by a space: ")
nums = [int(n) for n in nums.split(' ')]

for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if int(nums[j]) > int(nums[j + 1]):
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
