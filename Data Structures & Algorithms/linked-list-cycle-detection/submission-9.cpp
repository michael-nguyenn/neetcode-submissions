/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution 
{
public:
    bool hasCycle(ListNode* head) 
    {
        ListNode* dummy = new ListNode(-1, head);
        ListNode* fast = head;
        ListNode* slow = dummy;

        while (fast && fast->next && fast->next->next)
        {
            if (fast == slow) { return true; }

            fast = fast->next->next;
            slow = slow->next;
        }

        return false;
    }
};
