#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class RandomizedCollection {
    private:
    unordered_map<int, unordered_set<int>> index;
    vector<int>                            nums;

    public:
    /** Initialize your data structure here. */
    RandomizedCollection() {
    }

    /** Inserts a value to the collection. Returns true if the collection did
     * not already contain the specified element. */
    bool insert(int val) {
        nums.push_back(val);
        index[val].insert(nums.size() - 1);
        return index[val].size() == 1;
    }

    /** Removes a value from the collection. Returns true if the collection
     * contained the specified element. */
    bool remove(int val) {
        if (index.find(val) == index.end()) {
            return false;
        }
        auto i  = *index[val].begin();
        nums[i] = nums.back();
        index[val].erase(i);
        index[nums[i]].erase(nums.size() - 1);

        if (i < nums.size() - 1) {
            index[nums[i]].insert(i);
        }
        if (index[val].size() == 0) {
            index.erase(val);
        }
        nums.pop_back();
        return true;
    }

    /** Get a random element from the collection. */
    int getRandom() {
        return nums[rand() % nums.size()];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */