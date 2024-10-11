# LeetCode 297 - Serialize and Deserialize Binary Tree - HARD
# In this problem, we are required to serialize a binary tree into a string. We can then pass that string
# to the deserialize method to recreate the binary tree. 
# Serialize - In order serialize a binary tree, we can do a preorder representation of the BT. Using BFS, we can create
# a string of every value including Null values. This is all we need as it accounts for all nodes and their children
# Deserialize - To decode the received string, we KNOW that the first value is the root. We can use two deques to manage
# current nodes we are working on and the other for managing children. For each node, we know that the next two nodes 
# are its children. We can take the root node and set it's left and right children to the next two vals. If a value is not Null,
# we append it to the other deque, as those are parent nodes that need future set up. As we remove child node values and append them 
# as parents, we always maintain the order of children relative to current parents. Once we have worked through every parent node
# we have built the tree, and we just need to return the root node, which we need to save initially. 

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root) -> str:
        if not root:
            return ""
        dq = deque([root])
        serial = [str(root.val)]
        while dq:
            current = dq.popleft()
            if current.left:
                dq.append(current.left)
                serial.append(str(current.left.val))
            else:
                serial.append("None")
            if current.right:
                dq.append(current.right)
                serial.append(str(current.right.val))
            else: 
                serial.append("None")
        
        result = ','.join(serial)
        return result
                    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str):
        if not data:
            return
        # this is the child node string values
        dataDq = deque(data.split(','))
        # this holds the parent nodes 
        remaining = deque(dataDq.popleft())
        root = None
        while remaining:
            current = remaining.popleft()
            if not root:
                current = TreeNode(int(current))
                root = current
            
            # Set the left child pointer and append it to the remaining parent deque
            # if it is not Null. 
            left = dataDq.popleft()
            if left != "None":
                left = TreeNode(int(left))
                current.left = left
                remaining.append(left)

            # Set the right child pointer and append it to the remaining parent deque if
            # it is not Null.
            right = dataDq.popleft()
            if right != "None":
                right = TreeNode(int(right))
                current.right = right
                remaining.append(right)
        
        return root


test = Codec()
n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(3)
n5 = TreeNode(1)
n6 = TreeNode(5)

n1.left, n1.right = n2, n3
n2.left  = n4
n3.left, n3.right = n5, n6

des = test.serialize(n1)
print(test.deserialize(des))
