# LeetCode - 17 - Combination of Phone Number - Medium
# For this problem, we are asked to create a function that returns all possible letter combinations based on a 
# series of digits based on telephone letter to digit mapping. 
# The function will receive a string of integer values.
# And it will return a list of strings
# This means that for any given number, there are 3 to 4 letters associated with that number. We can first create a hashMap
# to map digits to their letter characters.
# What we want to do then is to build every combination. That means that for 34, we would want to build every combination that starts
# with 'D' -> DG, DH, DI before moving on to 'E'. This means we need to iterate through each array one at a time to build the combinations.
# Because each combination will have the same number of characters as the original digit string, we know that our stopping point is once
# the build string is the same length as digits. 
# Because we need to build EVERY POSSIBLE combination, we know we need to use backtracking. 
# So, we can loop through the array, recursively calling the backtracking function on the next index. This will allow us to continue building
# our combination string one at a time for each letter relative to each digit! 
# The Time Complexity is O(n* m^n) where m is the amortized length of the lettermap arrays. 

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        lettermap = {
            "2": ['A', 'B', 'C'],
            "3": ['D', 'E', 'F'],
            "4": ['G', 'H', 'I'],
            "5": ['J', 'K', 'L'],
            "6": ['M', 'N', 'O'],
            "7": ['P', 'Q', 'R', 'S'],
            "8": ['T', 'U', 'V'],
            "9": ['W', 'X', 'Y', 'Z']
        }

        result = []
    
        def backtrack(index, builtLetters):
            if len(builtLetters) == len(digits):
                result.append(''.join(builtLetters))
                return
            
            letterArr = lettermap[digits[index]]

            for letter in letterArr:
                builtLetters.append(letter)
                backtrack(index + 1, builtLetters)
                builtLetters.pop()

        backtrack(0, [])
        return result

test = Solution()
s1 = "34"

print(test.letterCombinations(s1))








