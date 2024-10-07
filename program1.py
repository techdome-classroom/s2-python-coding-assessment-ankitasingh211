class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matching_brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            # If the character is a closing bracket
            if char in matching_brackets:
                # Pop the top of the stack if it's non-empty, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                
                if matching_brackets[char] != top_element:
                    return False
            else:
                
                stack.append(char)







    



  

