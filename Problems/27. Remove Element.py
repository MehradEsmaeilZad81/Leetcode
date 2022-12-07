nums = [int(num) for num in input().split()]
val = int(input())


def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


print(removeElement(nums, val))
