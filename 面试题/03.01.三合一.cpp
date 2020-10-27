#include <vector>
using namespace std;

class TripleInOne {
    private:
    vector<int> size;
    vector<int> data;
    int         stackSize;

    public:
    TripleInOne(int stackSize) {
        data            = vector<int>(3 * stackSize);
        size            = vector<int>(3, 0);
        this->stackSize = stackSize;
    }

    void push(int stackNum, int value) {
        if (size[stackNum] != stackSize) {
            data[stackNum * stackSize + size[stackNum]++] = value;
        }
    }

    int pop(int stackNum) {
        if (!isEmpty(stackNum)) {
            return data[stackNum * stackSize + --size[stackNum]];
        } else {
            return -1;
        }
    }

    int peek(int stackNum) {
        if (!isEmpty(stackNum)) {
            return data[stackNum * stackSize + size[stackNum] - 1];
        } else {
            return -1;
        }
    }

    bool isEmpty(int stackNum) {
        return !size[stackNum];
    }
};
