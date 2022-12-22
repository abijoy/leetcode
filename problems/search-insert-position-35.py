def search_insert(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2 
    while left < right:
        print(f'left: {left}, mid: {mid}, right: {right}')
        if target == nums[mid]:
            print(f'mid: {mid}')
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    print(f'\n\nleft: {left}, mid: {mid}, right: {right}')
    return mid if mid >= 0 and nums[mid] >= target else mid + 1

print(search_insert([1,3,5,6], target=7))