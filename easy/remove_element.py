def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    for i in range(len(nums)):
        for (index, i) in enumerate(nums):
            if i == val:
                nums.pop(index)
    return len(nums)
