#include <numeric>
#include <vector>
using namespace std;

// 并查集
class UF {
  public:
    vector<int> fa;
    vector<int> sz;
    int         n;
    int         comp_cnt;

  public:
    UF(int _n) : n(_n), comp_cnt(_n), fa(_n), sz(_n, 1) {
        iota(fa.begin(), fa.end(), 0);
    }

    int findset(int x) {
        return fa[x] == x ? x : fa[x] = findset(fa[x]);
    }

    bool unite(int x, int y) {
        x = findset(x);
        y = findset(y);
        if (x == y) {
            return false;
        }
        if (sz[x] < sz[y]) {
            swap(x, y);
        }
        fa[y] = x;
        sz[x] += sz[y];
        --comp_cnt;
        return true;
    }

    bool connected(int x, int y) {
        x = findset(x);
        y = findset(y);
        return x == y;
    }
};

class Solution {
  public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edgeList,
                                           vector<vector<int>>& queries) {
        int         s = queries.size(), l = edgeList.size();
        vector<int> qid(s);
        iota(qid.begin(), qid.end(), 0);
        sort(qid.begin(), qid.end(), [&queries](int i, int j) {
            return queries[i][2] < queries[j][2];
        });

        sort(edgeList.begin(), edgeList.end(),
             [](const auto& i, const auto& j) { return i[2] < j[2]; });

        UF           uf(n);
        int          i = 0;
        vector<bool> res(s);
        for (auto q : qid) {
            while (i < l && edgeList[i][2] < queries[q][2]) {
                uf.unite(edgeList[i][0], edgeList[i][1]);
                i++;
            }
            res[q] = uf.connected(queries[q][0], queries[q][1]);
        }

        return res;
    }
};
