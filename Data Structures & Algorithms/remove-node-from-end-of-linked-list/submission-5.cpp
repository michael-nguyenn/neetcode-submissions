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

// initialize two pointers, and keep them n steps apart from one another
// once we advance both to the end, the lower pointer will be at the element to remove
// if we introduce a dummy node and start the pointer there, it will then be at the element
// right before the one we want to remove. 
// the dummy node also handles the scenario where we have to remove the first node of our list 

class Solution 
{
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) 
    {
        ListNode dummy = ListNode(0, head);
        ListNode* right = head;
        ListNode* left = &dummy;

        // first we move the right pointer n steps
        // since n <= sz, the most right can do is point to nullptr, we won't ever
        // reference ->next as a nullptr
        for (int i = 0; i < n; i++)
        {
            right = right->next;
        }

        // now we move both pointers until right hits the end
        while (right)
        {
            right = right->next;
            left = left->next;
        }

        left->next = left->next->next;
        return dummy.next;

    }
};
