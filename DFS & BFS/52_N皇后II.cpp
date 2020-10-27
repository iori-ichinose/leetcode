#include <unordered_map>
using namespace std;

class Solution {
    private:
    unordered_map<int, bool> col;
    unordered_map<int, bool> diag1, diag2;
    int                      res;

    void getRes(int i, int n) {
        if (i == n) {
            res++;
            return;
        }
        for (int j = 0; j < n; j++) {
            if (col[j] || diag1[i - j] || diag2[i + j]) {
                continue;
            } else {
                col[j] = diag1[i - j] = diag2[i + j] = true;
                getRes(i + 1, n);
                col[j] = diag1[i - j] = diag2[i + j] = false;
            }
        }
    }

    public:
    int totalNQueens(int n) {
        getRes(0, n);
        return res;
    }
};