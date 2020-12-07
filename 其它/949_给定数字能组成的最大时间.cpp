#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
  public:
    string largestTimeFromDigits(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        string res = "";
        for (int i = 3; i >= 0; i--) {
            if (arr[i] > 2) {
                continue;
            }
            for (int j = 3; j >= 0; j--) {
                if (arr[i] == 2 && arr[j] > 3 || i == j) {
                    continue;
                }
                for (int k = 3; k >= 0; k--) {
                    if (k == i || k == j || arr[k] > 5) {
                        continue;
                    }
                    return to_string(arr[i]) + to_string(arr[j]) + ":" +
                           to_string(arr[k]) + to_string(arr[6 - i - j - k]);
                }
            }
        }
        return res;
    }
};