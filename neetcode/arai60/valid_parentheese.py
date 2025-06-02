import unittest
class Solution:
    def isValid(self, s: str) -> bool:
        parthness_stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                 print('call?')
                 parthness_stack.append(c)
            else:
                if not parthness_stack:
                    return False
                compare_char = parthness_stack.pop()
                if c == ')':
                  if compare_char == '(':
                      next
                  else:
                      return False
                if c == '}':
                  if compare_char == '{':
                      next
                  else:
                      return False
                if c == ']':
                  if compare_char == '[':
                      next
                  else:
                      print(compare_char)
                      return False
        return not parthness_stack and True
    

class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def test_valid(self):
        self.assertFalse(self.sol.isValid("(]"))

if __name__ == "__main__":
  unittest.main()