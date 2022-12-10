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
    print(f'left: {left}, mid: {mid}, right: {right}')

print(search_insert([1,3,5,7], target=8))