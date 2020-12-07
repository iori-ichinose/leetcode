#include <algorithm>
#include <string>
#include <vector>
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
    vector<char> res = {'z' + 1};

    int compare(vector<char>& s1, vector<char>& s2) {
        auto it1 = s1.rbegin(), it2 = s2.rbegin();
        while (it1 != s1.rend() && it2 != s2.rend()) {
            if (*it1 < *it2) {
                return -1;
            } else if (*it1 > *it2) {
                return 1;
            }
            it1++;
            it2++;
        }
        if (it1 == s1.rend() && it2 == s2.rend()) {
            return 0;
        } else if (it1 != s1.rend()) {
            return 1;
        } else {
            return -1;
        }
    }

    void dfs(TreeNode* root, vector<char>& path) {
        if (!root) {
            return;
        }
        path.push_back(root->val + 'a');
        if (!root->left && !root->right) {
            if (compare(path, res) < 0) {
                res = path;
            }
        }

        dfs(root->left, path);
        dfs(root->right, path);
        path.pop_back();
    }

  public:
    string smallestFromLeaf(TreeNode* root) {
        vector<char> path;
        dfs(root, path);
        return string(res.rbegin(), res.rend());
    }
};
