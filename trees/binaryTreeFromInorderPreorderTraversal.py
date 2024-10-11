# LeetCode 105 - Build a Binary Tree from Inorder and Preorder Traversal - Medium
#
# The preorder traversal is just the BFS traversal of a tree. That means that the first value in preorder
# will always be the root node. This means we ALWAYS know where to start from. With a BT, every row gets filled before moving
# to the next row but the order in which the final row is filled is unknown 
# Using the inorder traversal array, we can find a pivot point. The pivot point is the root. 
# Any values to the left of the root are the left subtree and any to the right of the root will be the right subtree
# the preorder array is the same. Because there will be n values to the left of the pivot and m values to the right,
# we can split the the preorder and inorder arrays such that:
# The right subtree is anything from the pivot point + 1 to the end [pivotpoint + 1:]
# The left subtree is anything up to the pivot point [:pivot point]
# The preorder traversal we need to remove the first value since it was the root and we already accounted for it!
# We can the recursively go through the provided arrays, building the left and right subtrees! Voila!!
# Time Complexity is O(n) since we need to go through every element of the array

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):

        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])
        
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                pivotPoint = i
                break
        
        leftInorder = inorder[:pivotPoint]
        rightInorder = inorder[pivotPoint + 1:]

        leftPreorder = preorder[1:pivotPoint + 1]
        rightPreorder = preorder[pivotPoint + 1:]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)
        return root


preorder=[5,3,1,2,4,6,7]
inorder=[1,2,3,4,5,6,7]

test = Solution()
print(test.buildTree(preorder, inorder))


            


                        




