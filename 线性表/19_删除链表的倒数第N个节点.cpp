#include <stack>
using namespace std;
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (n == 0 || !head || !head->next) {
            return nullptr;
        }

        ListNode*        phead = new ListNode(0, head);
        stack<ListNode*> stk;
        ListNode*        cur = phead;
        while (cur) {
            stk.push(cur);
            cur = cur->next;
        }
        for (int i = 0; i < n; ++i) {
            stk.pop();
        }
        ListNode* prev = stk.top();
        prev->next     = prev->next->next;
        ListNode* ans  = phead->next;
        delete phead;
        return ans;
    }

    ListNode* removeNthFromEnd_2(ListNode* head, int n) {
        ListNode* dummy  = new ListNode(0, head);
        ListNode* first  = head;
        ListNode* second = dummy;
        for (int i = 0; i < n; ++i) {
            first = first->next;
        }
        while (first) {
            first  = first->next;
            second = second->next;
        }
        second->next  = second->next->next;
        ListNode* ans = dummy->next;
        delete dummy;
        return ans;
    }
};
