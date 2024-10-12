# LeetCode 217 - Contains Duplicate - Easy
# For this easy problem, we just need to check to see if the array contains any duplicates
# We could use two loops for O(n^2) runtime. But let's just use a hashmap to memoize visited values

class Solution:
    def containsDuplicate(self, arr):
        visited = {}

        for ele in arr:
            if ele in visited:
                return True
            visited[ele] = ele
        
        return False