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
    inline int max(int a, int b) {
        return a > b ? a : b;
    }

    int findMaxDiff(TreeNode* root, int maxi, int mini) {
        if (!root) return 0;
        if (root->val > maxi) {
            maxi = root->val;
        } else if (root->val < mini) {
            mini = root->val;
        }

        if (!root->left && !root->right) {
            return maxi - mini;
        } else {
            return max(findMaxDiff(root->left, maxi, mini),
                       findMaxDiff(root->right, maxi, mini));
        }
    }

    public:
    int maxAncestorDiff(TreeNode* root) {
        return max(findMaxDiff(root->left, root->val, root->val),
                   findMaxDiff(root->right, root->val, root->val));
    }
};