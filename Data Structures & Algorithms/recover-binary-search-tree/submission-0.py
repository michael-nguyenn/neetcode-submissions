# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Problem
We're given the root of a binary search tree
- Two nodes were swapped by
- Have to find without altering the structure

- Inorder traversal on a BST gives you the nodes in sorted order
- Storing these in an array also gives you access to the nodes for swapping
- If two nodes were swapped there will be an "inversion" where i is > i+1.
    - If the nodes to be swapped are beside each other there will be one inversion
    - If the nodes are further apart, there will be two instances of inversions
        - In that case the element of the first inversion is our first ele
        - and the second element of the second inversion is the second ele

Example 
- [2,5,9,10,11,14,12]
    - Here there is one inversion, so 14 and 12 are to be swapped
- [2,5,9,10,14,12,11]
    - 14, 12 is our first inversion
    - 12, 11 is our second inversion
    - So 14 and 11 are our elements tos wap

Strategy
- Go thru our tree in inorder, left, visit, right
- Append the entire node to an array
- Go thru the array from 0-len(array), stepping by 2
- Compare node's val i to i+1
- We're guaranteed to find at least one inversion, and break before we run into an index error

"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        inorder = []
        first_idx, second_idx = -1, -1

        def inorder_traversal(root):
            if not root:
                return

            inorder_traversal(root.left)
            inorder.append(root)
            inorder_traversal(root.right)
            
        inorder_traversal(root)

        for i in range(0, len(inorder)-1):
            if inorder[i].val > inorder[i+1].val:
                if first_idx == -1:
                    first_idx = i
                second_idx = i+1
        
        inorder[first_idx].val, inorder[second_idx].val = inorder[second_idx].val, inorder[first_idx].val


        
        