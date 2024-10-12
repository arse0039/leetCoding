# This is a hard question that we could use two heaps for. One for the right side of the median. One for the left
# But that makes it O(n + log n) run time. If we just sort the list, we get a O(n log n) runtime. 
# Not a huge difference IMO so keep it simple. If we scale and it gets crazy, we can always go back and refactor...

class MedianFinder:

    def __init__(self):
        self.values = []
        
    def addNum(self, num: int) -> None:
        self.values.append(num)

    def findMedian(self) -> float:
        self.values.sort()
        medIndex = len(self.values) // 2
        if not len(self.values) % 2:
            medIndex2 = len(self.values) // 2 - 1
            return (self.values[medIndex] + self.values[medIndex2])/2
        else: 
            return self.values[medIndex]

test = MedianFinder()
test.addNum(1)
test.addNum(2)
print(test.findMedian())