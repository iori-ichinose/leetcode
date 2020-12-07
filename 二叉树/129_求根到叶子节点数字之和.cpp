#include <queue>
using namespace std;
// Definition for a binary tree node.
struct TreeNode {
    int       val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {
    }
};

class Solution {
    private:
    int bfs(TreeNode* root) {
        if (!root) {
            return 0;
        }
        int              res = 0;
        queue<TreeNode*> nodes;
        queue<int>       nums;

        nodes.push(root);
        nums.push(root->val);
        while (!nodes.empty()) {
            auto node = nodes.front();
            auto num  = nums.front();
            nodes.pop();
            nums.pop();
            if (!node->left && !node->right) {
                res += num;
            } else {
                if (node->left) {
                    nodes.push(node->left);
                    nums.push(num * 10 + node->left->val);
                }
                if (node->right) {
                    nodes.push(node->left);
                    nums.push(num * 10 + node->left->val);
                }
            }
        }
        return res;
    }

    int dfs(TreeNode* root, int cur_sum) {
        if (!root) {
            return 0;
        }
        if (!root->left && !root->right) {
            return cur_sum * 10 + root->val;
        }

        return dfs(root->left, cur_sum * 10 + root->val) +
               dfs(root->right, cur_sum * 10 + root->val);
    }

    public:
    int sumNumbers(TreeNode* root) {
        return dfs(root, 0);
    }
};
