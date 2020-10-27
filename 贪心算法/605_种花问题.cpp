// https://leetcode-cn.com/problems/can-place-flowers/
// 隔一个种花实质上就是每三个空格种一朵。
// 可以在队列开头与结尾加上'0'，从而能简化判断。

#include <vector>
using namespace std;

class Solution {
    public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        flowerbed.insert(flowerbed.begin(), 0);
        int count = 0;
        flowerbed.push_back(0);
        for (auto i = flowerbed.begin() + 1; i < flowerbed.end() - 1; i++) {
            if (*i == 0 && *(i - 1) == 0 && *(i + 1) == 0) {
                if (++count >= n) {
                    return true;
                }
                i++;
            }
        }
        return false;
    }
};
