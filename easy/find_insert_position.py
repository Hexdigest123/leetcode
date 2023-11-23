nums = [1,3,5,6]
target = 2

# slow and memory inefficient
def searchInsert(nums, target):
    for (index, i) in enumerate(nums):
        if i == target:
            return index
    for (index, i) in enumerate(nums):
        if i > target:
            return index
    return len(nums)


# faster and more memory efficient
def searchInsert_2(nums, target):
    for (index, i) in enumerate(nums):
        if i >= target:
            return index
    return len(nums)



print(searchInsert_2(nums, target))