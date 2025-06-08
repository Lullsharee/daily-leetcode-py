import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in '({[':
                stack.append(char)
            elif not stack or char != brackets[stack.pop()]:
                return False

        return not stack


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_valid(self):
        self.assertFalse(self.sol.isValid("(]"))


if __name__ == "__main__":
    unittest.main()