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
        inorder_dfs(root);
        return res;
    }

    void inorder_dfs(TreeNode* root)
    {
        if (!root || nodes_left == 0) { return; }

        inorder_dfs(root->left);

        if (--nodes_left == 0)
        {
            res = root->val;
            return;
        }

        inorder_dfs(root->right);
    }
};
