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

// we need a min heap that will hold at most k items
// each of the k will represent a valid head of the k linked lists
// we'll iterate until the min heap is empty, that means we've consumed all k linked lists

class Solution 
{
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) 
    {
        auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
        std::priority_queue<ListNode*, std::vector<ListNode*>, decltype(cmp)> minHeap(cmp);
        ListNode dummy(0); // we'll return this at the end

        // now we have to go thru lists and append each non null node to our priority q
        for (ListNode* node : lists)
        {
            if (node)
            {
               minHeap.push(node); 
            }
        }

        // at this point we hold at most a k sized min heap with the heads of each ll
        ListNode* cur = &dummy;
        while (!minHeap.empty())
        {
            // get the smallest node
            ListNode* smallest = minHeap.top();
            minHeap.pop();

            cur->next = smallest;
            cur = cur->next;

            // if LL containing smallest has another element we want to refil our minheap
            if (smallest->next)
            {
                minHeap.push(smallest->next);
            }
        }

        return dummy.next;

    }
};
