#include <set>
using namespace std;

class MyCalendar {
  private:
    set<pair<int, int>> schedule;

  public:
    MyCalendar() {
    }

    bool book(int start, int end) {
        for (auto& date : schedule) {
            if (start < date.second && end > date.first) {
                return false;
            }
        }
        schedule.emplace(start, end);
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
