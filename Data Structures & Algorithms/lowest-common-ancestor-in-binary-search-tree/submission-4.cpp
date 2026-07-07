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

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* cur = root;

        while (cur) {
            // if cur is less than both nodes then need to go right to find
            if (cur->val < p->val && cur->val < q->val) {
                cur = cur->right;
            } else if (cur->val > p->val && cur->val > q->val) {
                cur = cur->left;
            } else {
                // in this case we're at the lowest common ancestor
                return cur;
            }
        }

        return nullptr; // we'll never hit this
    }
};
