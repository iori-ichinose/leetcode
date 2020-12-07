
// Definition for singly-linked list.
struct ListNode {
    int       val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {
    }
};

class Solution {
  public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* p0  = new ListNode(0);
        p0->next      = head;
        ListNode *pre = p0, *p = head;
        ListNode* tmp;
        while (p) {
            if (p->val == val) {
                pre->next = p->next;
                tmp       = p;
                p         = p->next;
                delete tmp;
            } else {
                pre = p;
                p   = p->next;
            }
        }
        return p0->next;
    }
};
