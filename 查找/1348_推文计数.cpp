#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

class TweetCounts {
  private:
    map<string, set<int>> user;

  public:
    TweetCounts() {
    }

    void recordTweet(string tweetName, int time) {
        user[tweetName].insert(time);
    }

    vector<int> getTweetCountsPerFrequency(string freq, string tweetName,
                                           int startTime, int endTime) {
        int length;
        if (freq == "minute") {
            length = 60;
        } else if (freq == "hour") {
            length = 60 * 60;
        } else {
            length = 60 * 60 * 24;
        }

        vector<int> res((endTime - startTime) / length + 1);

        auto begin = user[tweetName].lower_bound(startTime),
             end   = user[tweetName].upper_bound(endTime);
        for (; begin != end; begin++) {
            res[(*begin - startTime) / length]++;
        }

        return res;
    }
};

/**
 * Your TweetCounts object will be instantiated and called as such:
 * TweetCounts* obj = new TweetCounts();
 * obj->recordTweet(tweetName,time);
 * vector<int> param_2 =
 * obj->getTweetCountsPerFrequency(freq,tweetName,startTime,endTime);
 */