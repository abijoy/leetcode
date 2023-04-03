
# TWO POINTERS
# linera time solution
def maxArea(height) -> int:
    left, right = 0, len(height) -1

    res = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        res = area if area > res else res

        # update the pointers 
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return res