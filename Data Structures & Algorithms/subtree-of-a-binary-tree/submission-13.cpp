/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

// we need to fist search the main tree until we land on a node the same as subroot
// if we make it all the way down to null in the main tree it means we've exhausted our search
// and the subroot does not exist in the tree

class Solution 
{
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) 
    {
        if (!root) { return false; }

        // If the two match, then we can call isSameTree 
        // that function will also return a boolean
        // if is comes back false, that's ok, we'll keep exploring
        // if it comes back true, then we know the subtree exists, and we can cascade a true up
        if (root->val == subRoot->val) 
        {
            if (isSameTree(root, subRoot))
            {
                return true;
            }
        }

        // otherwise we keep searching to find matching roots
        if (isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot))
        {
            return true;
        }

        return false;
    }

    bool isSameTree(TreeNode* node1, TreeNode* node2)
    {
        // both null is same tree, if one is null then they're different
        if (!node1 && !node2) { return true; }
        if (!node1 || !node2) { return false; }

        if (node1->val != node2->val) { return false; }

        // now if they're matching we recurse down
        return isSameTree(node1->left, node2->left) && isSameTree(node1->right, node2->right);    

    }
};
