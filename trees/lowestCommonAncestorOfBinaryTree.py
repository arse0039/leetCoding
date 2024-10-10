class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This is solution that uses DFS to search the tree for matching nodes. When a node has a value of 2, meaning we have
# have found the two nodes, we save the node until the dfs ends. This solution is O(n) since it searches the entire tree
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        ancestor = None

        def dfs(node):
            nonlocal ancestor 

            if not node:
                return 0
            
            # left
            left = dfs(node.left)
            right = dfs(node.right)

            current = 0
            if node.val == p.val or node.val == q.val:
                current += 1
            if left + right + current == 2:
                ancestor = node
                return 0
            else:
                return left + right + current
            
        dfs(root)
        return ancestor


# this is a better solution that does not traverse the entire tree. It cuts it in half each time
# so it is O(log n).
class Solution2:
    def lowestCommonAncestor(self, root, p, q):
        
        while True:
            if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
                return root
            elif q.val < root.val > p.val:
                root = root.left
            elif q.val > root.val < p.val:
                root = root.right


test = Solution()
n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(8)
n4 = TreeNode(1)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(9)
n8 = TreeNode(2)

n1.left, n1.right = n2, n3
n2.left, n2.right = n4, n5
n3.left, n3.right = n6, n7
n4.right = n8

test.lowestCommonAncestor(n1, n4, n8)