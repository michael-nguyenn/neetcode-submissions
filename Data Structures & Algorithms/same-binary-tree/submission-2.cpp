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

// at a given node provided everything else matches, then the work we must do at a given node
// is comparing the values of one another

class Solution 
{
public:
    bool isSameTree(TreeNode* p, TreeNode* q) 
    {
        // if both nodes are null, then it's a match
        if (!p && !q) { return true; }
        if (!p && q) { return false; }
        if (!q && p) {return false; }


        if (!isSameTree(p->left, q->left) || !isSameTree(p->right, q->right)) 
        { 
            return false; 
        }
        else
        {
            return p->val == q->val;
        }
    }
};
