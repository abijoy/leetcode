# iteration method
def remove_duplicates(nums) -> int:
    k = 0
    prev = -101
    k = 0
    next_spot = 0
    for i in range(len(nums)):
        if nums[i] != prev:
            nums[next_spot] = nums[i]
            next_spot += 1
        prev = nums[i]
    return nums[:next_spot]


# set method
def remove_duplicates_set(nums) -> int:
    return len(set(nums))

# remove_duplicates([0,0,1,1,1,2,2,3,3,4])
remove_duplicates([1,2,5])
print(remove_duplicates_set([0,0,1,1,1,2,2,3,3,4]))