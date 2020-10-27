#include <stack>
#include <vector>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int       val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {
    }
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {
    }
    TreeNode(int x, TreeNode* left, TreeNode* right)
        : val(x), left(left), right(right) {
    }
};

class Solution {
    public:
    vector<int> preorderTraversal(TreeNode* root) {
        if (!root) {
            return {};
        }
        stack<TreeNode*> st;
        vector<int>      res;
        st.push(root);
        while (!st.empty()) {
            auto cur = st.top();
            st.pop();

            res.emplace_back(cur->val);
            if (cur->right) {
                st.push(cur->right);
            }
            if (cur->left) {
                st.push(cur->left);
            }
        }
        return res;
    }
};
