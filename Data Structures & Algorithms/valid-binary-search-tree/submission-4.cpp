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

#include <cmath>

// so to satisfy the BST we have to ensure that at any given node
// the left child is less than the node
// the right child is greater than the node

// we'll need to pass in a range the child must satisfy

class Solution 
{
public:
    bool isValidBST(TreeNode* root) 
    {
        return validate(root, -INFINITY, INFINITY);
    }

    bool validate(TreeNode *root, float low_bound, float high_bound)
    {
        if (!root) { return true; }
        if (root->val <= low_bound || root->val >= high_bound) { return false; }

        return validate(root->left, low_bound, root->val) && validate(root->right, root->val, high_bound);
    }
};
