class Solution {
  public:
    double angleClock(int hour, int minutes) {
        auto   abs        = [](auto x) { return x > 0 ? x : -x; };
        auto   min        = [](auto x, auto y) { return x < y ? x : y; };
        double min_angle  = minutes * 6,
               hour_angle = hour % 12 * 30 + minutes / 2.0;
        double res        = abs(hour_angle - min_angle);
        return min(res, 360 - res);
    }
};
