hashmap = {}


def majorityElement(nums) -> int:
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1

    for key, value in hashmap.items():
        if value > len(nums) / 2:
            return key
    return -1


print(majorityElement([2,2,1,1,1,2,2]))
