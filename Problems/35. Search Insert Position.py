nums = [int(num) for num in input().split()]
target = int(input())

def SearchInsertPosition(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in range(len(nums)):
            if nums[i] > target:
                return i
        return len(nums)
    
print(SearchInsertPosition(nums, target))