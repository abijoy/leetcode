
# check if a number is a palindrome without converting it into string.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        
        # we just need to check if two halves are equal
        # to be a palindrome number
        half = 0
        while x > half:
            # move last digit of x onto half
            half = (half * 10) + (x % 10)
            
            # update x
            x = x // 10
        return x == half or x == half // 10
