nums = [int(num) for num in input().split()]
target = int(input())


def twoSum(nums, target):
    tmp = {}
    for i, num in enumerate(nums):
        if target - num in tmp:
            return [tmp[target - num], i]
        tmp[num] = i
    return [-1, -1]


print(twoSum(nums, target))