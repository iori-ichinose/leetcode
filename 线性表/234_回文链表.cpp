#include <vector>
using namespace std;
// Definition for singly-linked list.
struct ListNode {
    int       val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {
    }
};

/*
class Solution {
    public:
    bool isPalindrome(ListNode* head) {
        ListNode*   p = head;
        vector<int> list;
        while (p) {
            list.emplace_back(p->val);
            p = p->next;
        }
        for (int i = 0, j = list.size() - 1; i < j; i++, j--) {
            if (list[i] != list[j]) {
                return false;
            }
        }

        return true;
    }
};
*/

class Solution {
    private:
    ListNode* getMidNode(ListNode* head) {
        ListNode *fast = head, *slow = head;
        while (fast->next && fast->next->next) {
            fast = fast->next->next;
            slow = slow->next;
        }
        return slow;
    }

    ListNode* reverseNodes(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* nextTemp = curr->next;
            curr->next         = prev;
            prev               = curr;
            curr               = nextTemp;
        }
        return prev;
    }

    public:
    bool isPalindrome(ListNode* head) {
        if (head == nullptr) {
            return true;
        }

        // 找到前半部分链表的尾节点并反转后半部分链表
        ListNode* firstHalfEnd    = getMidNode(head);
        ListNode* secondHalfStart = reverseNodes(firstHalfEnd->next);

        // 判断是否回文
        ListNode* p1     = head;
        ListNode* p2     = secondHalfStart;
        bool      result = true;
        while (result && p2 != nullptr) {
            if (p1->val != p2->val) {
                result = false;
            }
            p1 = p1->next;
            p2 = p2->next;
        }

        // 还原链表并返回结果
        // firstHalfEnd->next = reverseList(secondHalfStart);
        return result;
    }
};