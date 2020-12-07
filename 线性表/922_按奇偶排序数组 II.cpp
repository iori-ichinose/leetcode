#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        int n = A.size();
        for (int i = 0, j = 1; i < n; i += 2) {
            if (A[i] & 1) {
                for (; A[j] & 1 && j < n; j += 2)
                    ;
                swap(A[i], A[j]);
            }
        }
        return A;
    }
};
