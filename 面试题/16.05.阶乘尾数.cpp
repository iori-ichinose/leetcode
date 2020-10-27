// https://leetcode-cn.com/problems/factorial-zeros-lcci/
// 结果的中的尾随0都是由5与2贡献的，因此只要找出每个n中5的因数个数即可。

class Solution {
    public:
    int trailingZeroes(int n) {
        int res = 0;
        while (n >= 5) {
            n /= 5;
            res += n;
        }
        return res;
    }
};
