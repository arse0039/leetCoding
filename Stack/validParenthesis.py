"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Can s be and empty string? Yes

{([()])}

"""

class Solution:
    def validParenthesis(self, s:str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        validMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
         }
        queue = []

        for char in s:
            if char not in validMap:
                queue.append(char)
            else:
                if not queue: 
                    return False
                match = queue.pop()
                if validMap[char] != match:
                    return False
        
        return True if not queue else False

test = Solution()
s1 = "[]"

print(test.validParenthesis(s1))



