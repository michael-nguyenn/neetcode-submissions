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
#include <queue>

class Solution 
{
public:
    vector<vector<int>> levelOrder(TreeNode* root) 
    {
        std::queue<TreeNode*> q;
        std::vector<vector<int>> res;

        // if the root exists we can add it to our q
        if (root) 
        {
            q.push(root);
        }

        // then we'll go thru the q level by level
        while (!q.empty())
        {
            // need to capture just the initial length of the q
            int cur_len = static_cast<int>(q.size());
            std::vector<int> level_entries;

            // while q at level has elements
            for (int i = 0; i < cur_len; i++)
            {
                TreeNode* cur_node = q.front();
                q.pop();
                level_entries.push_back(cur_node->val);

                // add children to q
                if (cur_node->left) { q.push(cur_node->left); }
                if (cur_node->right) { q.push(cur_node->right); }
            }

            // at the end of the level, append the q to the res
            res.push_back(level_entries);
        }

        return res;
        
    }
};