# LeetCode 621 - TaskScheduler - Medium
# This one is a doozy! We are tasked with finding the minimum number of operations it would take
# to process all tasks in a received array of tasks. The same task can not be performed within 'n' operations.
# The biggest thing to realize with this problem is that the string values don't matter. We just need to reduce everything
# down to values. We have a specific number of each task type. To be the most efficient, we always want to process whatever
# task has the largest number of tasks in the queue first. This means a maxHeap will work wonders for us! 
# When we process a task, it needs to be removed from the processing list (maxHeap) BUT we need to readd it when it is able to
# be processed again! To achieve this, we can create a deque and add completed tasks as we remove them from our maxHeap. We can
# add them to our deque along with the time they can be readded to our maxHeap by adding the current time value to the 
# n value. As we increment our time, we can compare the deque time. If it is a match, we can pop that bad boy and add the value to the 
# maxHeap and keep on keeping on!

from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        countHash = Counter(tasks)
        dq = deque([])
        maxHeap = [-count for count in countHash.values()]
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap or dq:
            # if we have something in our maxHeap, that means it can be processed. So we want to
            # process the largest value. Shrink it by 1, and, if we haven't used it all up, add it to
            # our deque along with the time it can be reintroduced into the task heap. 
            if maxHeap:
                largest = heapq.heappop(maxHeap)
                largest += 1
                if largest < 0:
                    dq.append((largest, time + n))                
            
            # if we have a deque and the top-most item in our deque has a time that matches the 
            # current time, this means it's able to be readded to our scheduler heap!
            if dq and dq[0][1] == time:
                remaining, time = dq.popleft()
                heapq.heappush(maxHeap, remaining)
            # no matter what happens, each iteration of the loop represents a task cycle. 
            time += 1

        return time

tasks = ["A","A","A","B","C"]
n = 3
        
test = Solution()
print(test.leastInterval(tasks, n))

        


        