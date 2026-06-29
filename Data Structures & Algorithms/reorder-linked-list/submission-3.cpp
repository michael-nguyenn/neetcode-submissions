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

// this problem is essentially asking for us to interleave the linked list
// one from the front, one from the back, etc etc 

// that can be reframed into three primary parts
// need to split the array into two halves
// reverse the second half
// merge the two together

class Solution 
{
public:
    void reorderList(ListNode* head) 
    {
        if (!head->next) { return; }
        // use a fast & slow pointer to get the half way part
        // we'll start fast one above, which lands slow at the end of the first half
        // odd len linked lists will have slow longer by one which is fine since we
        // interleave with slow first
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast && fast->next)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        // At the end of that slow is the last node in the first half
        ListNode* cur = slow->next;
        slow->next = nullptr; // this breaks the two LLs apart

        // Now we reverse our second half
        ListNode* prev = nullptr;
        while (cur)
        {
            ListNode* next = cur->next;
            cur->next = prev;
            prev = cur;
            cur = next;
        }

        // prev will now hold the new head of our reversed list
        cur = head;
        ListNode* cur2 = prev;
        while (cur2)
        {
            ListNode* next = cur->next;
            ListNode* next2 = cur2->next;

            cur->next = cur2;
            cur2->next = next;

            cur = next;
            cur2 = next2;
        }

    }
};
