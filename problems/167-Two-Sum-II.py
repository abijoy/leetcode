def twoSum(numbers, target: int):
    first = 0
    last = len(numbers) - 1
    while first < last:
        res = numbers[first] + numbers[last]
        if res > target:
            last -= 1
        elif res < target:
            first += 1
        else:
            return [first+1, last+1]