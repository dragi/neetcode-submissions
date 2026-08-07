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

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == nullptr)
            return nullptr;
        
        ListNode* curr = head;
        int len = 0;
        while (curr != nullptr) {
            ++len;
            curr = curr->next;
        }
        
        int index = len - n;
        if (index == 0)
            return head->next;
        
        curr = head;
        int i = 0;
        while (i < index - 1) {
            curr = curr->next;
            ++i;
        }
        curr->next = curr->next->next;
        
        return head;
    }
};
