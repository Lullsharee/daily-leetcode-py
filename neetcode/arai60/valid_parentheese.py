import unittest
class Solution:
  def isValid(self, s: str) -> bool:
    parthness_stack = []
    parthness_dict = dict(('()', '{}', '[]'))

    for c in s:
        if c in '({[':
           parthness_stack.append(c)
        elif not parthness_stack or c != parthness_dict[parthness_stack.pop()]:
           return False
        
    return not parthness_stack

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def test_valid(self):
        self.assertFalse(self.sol.isValid("(]"))

if __name__ == "__main__":
  unittest.main()