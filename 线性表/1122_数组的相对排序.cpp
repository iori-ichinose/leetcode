#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> rank;
        int                     n = arr2.size();
        for (int i = 0; i < n; i++) {
            rank[arr2[i]] = i - n;
        }
        sort(arr1.begin(), arr1.end(), [&rank](int x, int y) -> bool {
            return (rank.count(x) ? rank[x] : x) <
                   (rank.count(y) ? rank[y] : y);
        });
        return arr1;
    }
};
