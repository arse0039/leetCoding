class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        

        def helper(p, q):
        
            if not p and not q:
                return True

            nodeP = p.val if p else None
            nodeQ = q.val if q else None

            if nodeP != nodeQ:
                return False
            
            left = helper(p.left, q.left)
            right = helper(p.right, q.right)

            return (left and right)

        
        return helper(p, q)