class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Solution
        return str(x) == str(x)[::-1]
        