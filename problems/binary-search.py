def binary_search(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = ( left + right ) // 2
        print(f'{left=} {mid=} {right=}')
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
        print(f'{left=} {mid=} {right=}')
        print()
    return False

print(binary_search([1,3,5,7,9], target=10))