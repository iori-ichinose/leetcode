
// Definition for singly-linked list.
struct ListNode {
    int       val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {
    }
    ListNode(int x) : val(x), next(nullptr) {
    }
    ListNode(int x, ListNode* next) : val(x), next(next) {
    }
};

class Solution {
    public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* p    = new ListNode;
        auto      head = p;
        int       s    = 0;
        while (l1 || l2 || s) {
            s += (l1 ? l1->val : 0) + (l2 ? l2->val : 0);
            p->next = new ListNode(s % 10);
            s /= 10;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return head->next;
    }
};