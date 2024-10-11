# LeetCode 124 - Binary Tree Maximum Path Sum - HARD
# In this problem, we need to find the largest max value of any path of nodes in the BT.
# This means that we need to have a running max value and perform a Depth-First Search on the tree
# For every node, we need to compare the sum of its value plus both children to the maximum value to see if it is greater.
# If it is, great! We update our max value. Otherwise, no big deal. To continue up, we can use the sums of both children because that
# is NOT a linear path. We need to find the largest value between the left child + the current node vs the right child + current. 
# Whichever is larger is what we want to pass. We also need to account for negative values. If both children are negative integers,
# we want to just take the nodes current value and pass it up. Once we have done this for every node using DFS, we should have our
# max value, which we can return back to the user!

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        maxResult = root.val

        def dfs(node):
            nonlocal maxResult

            if not node:
                return 0
            
            left = dfs(node.left) 
            right = dfs(node.right)

            currentS = node.val
            
            if left and currentS + left > currentS:
                currentS = currentS + left
            if right and currentS + right > currentS:
                currentS = currentS + right
            
            maxResult = max(maxResult, currentS)

            currentNSLeft = node.val
            currentNSRight = node.val
            if left and node.val + left > node.val:
                currentNSLeft = node.val + left
            if right and node.val + right > node.val:
                currentNSRight = node.val + right

            return max(currentNSLeft, currentNSRight)

        dfs(root)
        return maxResult



test = Solution()

n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(1)

n1.left, n1.right = n2, n3
n2.left = n4 
n3.left, n3.right = n5, n6
n4.left, n4.right = n7, n8
n6.right = n9
print(test.maxPathSum(n1))