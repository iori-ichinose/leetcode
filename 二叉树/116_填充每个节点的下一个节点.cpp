#include <queue>
using namespace ::std;
// Definition for a Node.
class Node {
    public:
    int   val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {
    }

    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {
    }

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {
    }
};

class Solution {
    public:
    Node* connect(Node* root) {
        if (!root) return nullptr;
        queue<Node*> q;
        q.push(root);
        while (!q.empty()) {
            auto size = q.size();
            for (int i = 0; i < size; i++) {
                auto node = q.front();
                q.pop();

                if (i < size - 1) {
                    node->next = q.front();
                }
                if (node->left) {
                    q.push(node->left);
                }
                if (node->right) {
                    q.push(node->right);
                }
            }
        }
        return root;
    }
};