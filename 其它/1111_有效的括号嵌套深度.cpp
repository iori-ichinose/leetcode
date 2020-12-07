#include <string>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> maxDepthAfterSplit(string seq) {
        int         depth = 0;
        vector<int> res;
        for (char ch : seq) {
            if (ch == '(') {
                depth++;
                res.push_back(depth % 2);
            } else {
                res.push_back(depth % 2);
                depth--;
            }
        }
        return res;
    }
};
