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
    std::vector<int> preorder_vec{};

public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) 
    {
        for (size_t i = 0; i < inorder.size(); i++)
        {
            inorder_map[inorder[i]] = i;
        }

        preorder_vec = preorder;
        return build(0, static_cast<int>(inorder.size()) - 1);
    }

    TreeNode* build(int left, int right)
    {
        if (left > right)
        {
            return nullptr;
        }

        int root_val = preorder_vec[pre_idx];
        pre_idx++;

        TreeNode* root = new TreeNode(root_val);
        int mid = inorder_map[root_val];

        root->left = build(left, mid - 1);
        root->right = build(mid + 1, right);
        return root;
    }
};
