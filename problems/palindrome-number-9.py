# check palindrome wihout converting it in string
def isPalindrome(x: int) -> bool:
    digits = []
    num = x
    while x > 0:
        # print(x % 10, end=" ")
        digits.append(x % 10)
        x = x // 10
    multiplier = 1
    rev_num = 0
    for d in reversed(digits):
        rev_num += d * multiplier
        multiplier *= 10
    print(num)
    print(digits)
    print(rev_num)
    return num == rev_num
    
print(isPalindrome(-121))