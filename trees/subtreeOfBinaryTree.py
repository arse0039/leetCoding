# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot or not root:
            return False
        
        matches = []
        

        #recursive function to find a matching node
        def findMatch(node, root):
            nonlocal matches

            if not node:
                return
            
            if node.val == root.val:
                matches.append(node)

            findMatch(node.left, root)
            findMatch(node.right, root)
        
        findMatch(root, subRoot)
        
        def dfs(node, subNode):
            if not node and not subNode:
                return True
            
            nodeVal = node.val if node else None
            subNodeVal = subNode.val if subNode else None

            if nodeVal != subNodeVal:
                return False
            
            left = dfs(node.left, subNode.left)
            right = dfs(node.right, subNode.right)

            return left and right
        
        answer = False
        for node in matches:
            answer = dfs(node, subRoot) or answer
        
        return answer

test = Solution()

tree = [1, 2, 3, 4, 5]
subtree = [2, 4, 5]
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5

s1 = TreeNode(2)
s2 = TreeNode(4)
s3 = TreeNode(5)
s1.left, s1.right = s2, s3

print(test.isSubtree(n1, s1))

