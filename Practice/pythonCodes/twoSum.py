def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []

nums = [1, 2, 7, 11, 15]
target = 9
res = twoSum(nums, target)
print(res)
print(target)
                