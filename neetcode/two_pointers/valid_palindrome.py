from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        replace_s = ''.join(e for e in s if e.isalnum()).lower()
        left, right = 0, len(replace_s) - 1
        while left < right:
            if replace_s[left] != replace_s[right]:
                return False
            left += 1
            right -= 1
        return True
    