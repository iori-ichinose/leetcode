#include <cmath>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> powerfulIntegers(int x, int y, int bound) {
        unordered_set<int> hashtable;
        for (int i = 0;; i++) {
            int newx = (int)pow(x, i);
            if (newx >= bound)
                break;
            for (int j = 0;; j++) {
                int newy = (int)pow(y, j);
                if (newx + newy > bound)
                    break;
                hashtable.insert(newx + newy);
                if (y == 1)
                    break;
            }
            if (x == 1)
                break;
        }
        return vector<int>(hashtable.begin(), hashtable.end());
    }
};