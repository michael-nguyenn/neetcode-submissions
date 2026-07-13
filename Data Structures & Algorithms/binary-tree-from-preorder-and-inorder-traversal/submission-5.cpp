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
    size_t pre_idx = 0;
    std::unordered_map<int, int> inorder_map {};

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) 
    {
        for (size_t i = 0; i < inorder.size(); i++)
        {
            inorder_map[inorder[i]] = i;
        }

        return build(preorder, 0, static_cast<int>(inorder.size()) - 1);
    }

    TreeNode* build(const std::vector<int>& preorder, int left, int right)
    {
        if (left > right)
        {
            return nullptr;
        }

        int root_val = preorder[pre_idx];
        pre_idx++;

        TreeNode* root = new TreeNode(root_val);
        int mid = inorder_map[root_val];

        root->left = build(preorder, left, mid - 1);
        root->right = build(preorder, mid + 1, right);
        return root;
    }
};
