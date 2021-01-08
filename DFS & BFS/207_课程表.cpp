#include <vector>
using namespace std;

class Solution {
  private:
    enum class Identifer { Unvisited, Visiting, Visited };
    vector<vector<int>> edges;
    vector<Identifer>   visited;
    bool                valid;

    void dfs(int u) {
        visited[u] = Identifer::Visiting;
        for (auto& edge : edges[u]) {
            if (visited[edge] == Identifer::Unvisited) {
                dfs(edge);
                if (!valid) {
                    return;
                }
            } else if (visited[edge] == Identifer::Visiting) {
                valid = false;
                return;
            }
        }
        visited[u] = Identifer::Visited;
    }

  public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        edges.resize(numCourses);
        visited.resize(numCourses);
        for (auto& info : prerequisites) {
            edges[info[1]].push_back(info[0]);
        }

        for (int i = 0; i < numCourses && valid; i++) {
            if (visited[i] == Identifer::Unvisited) {
                dfs(i);
            }
        }
        return valid;
    }
};
