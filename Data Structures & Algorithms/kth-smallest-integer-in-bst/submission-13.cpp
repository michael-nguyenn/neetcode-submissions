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

class Solution 
{
private:
    int nodes_left;
    int res;

public:
    int kthSmallest(TreeNode* root, int k) 
    {
        nodes_left = k;
        return inorder_dfs(root);
    }

    int inorder_dfs(TreeNode* root)
    {
        if (!root) { return 0; }
        if (nodes_left == 0) { return res; }

        inorder_dfs(root->left);

        nodes_left--;
        if (nodes_left == 0)
        {
            res = root->val;
        }

        inorder_dfs(root->right);
        return res;
    }
};
