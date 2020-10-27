#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        int n = A.size();
        vector<int> res(n);
        for (int start = 0, end = n - 1, pos = n - 1; pos >= 0; pos--) {
            if (-A[start] > A[end]) {
                res[pos] = A[start] * A[start];
                start++;
            } else {
                res[pos] = A[end] * A[end];
                end--;
            }
        }
        return res;
    }
};
