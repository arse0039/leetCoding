class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        cycleStr = str(n)
        while True:
            newVal = 0
            for char in cycleStr:
                newVal += int(char)**2
            
            if newVal == 1:
                return True
            
            if newVal in seen:
                return False
            else:
                seen[newVal] = newVal
            
            cycleStr = str(newVal)


test = Solution()
s1 = 19
test.isHappy(s1)