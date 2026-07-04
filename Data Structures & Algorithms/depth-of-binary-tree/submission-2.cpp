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

// so if we're at any given node, do determine the current depth would be the max between
// the two children, and then you want to return 1 + that to account for the node itself

class Solution 
{
public:
    int maxDepth(TreeNode* root) 
    {
        // a null node contributes nothing
        if (!root) { return 0; }

        return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
    }
};
