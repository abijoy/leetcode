def plus_one(digits):
    for i in reversed(range(len(digits))):
        reminder = 0
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            # num = digits[i] + 1
            digits[i] = 0
            reminder = 1
    return digits if reminder == 0 else [1] + digits

        
print(plus_one([9,9,9,9]))