#include <vector>
using namespace std;

class Solution {
    public:
    int videoStitching(vector<vector<int>>& clips, int T) {
        if (clips.empty()) {
            return 0;
        }
        vector<int> maxn(T);
        int         last(0), res(0), pre(0);
        for (auto& clip : clips) {
            if (clip[0] < T) {
                maxn[clip[0]] = max(maxn[clip[0]], clip[1]);
            }
        }

        for (int i = 0; i < T; i++) {
            last = max(last, maxn[i]);
            if (i == last) {
                return -1;
            } else if (i == pre) {
                res++;
                pre = last;
            }
        }
        return res;
    }
};
