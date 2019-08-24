#include <bits/stdc++.h>
using namespace std;

template <typename T>
struct Rectangle {
  pair<T, T> start, stop;
  Rectangle(T, T, T, T);
};
template <typename T>
Rectangle<T>::Rectangle(T start_x, T start_y, T stop_x, T stop_y)
    : start(start_x, start_y), stop(stop_x, stop_y) {}

template <typename T>
ostream &operator<<(ostream &o, const Rectangle<T> &r) {
  o << "[" << r.start.first << ", " << r.start.second << ", " << r.stop.first
    << ", " << r.stop.second << "]";
  return o;
}

template <typename T>
T area(Rectangle<T> r) {
  return abs(r.stop.first - r.start.first) * abs(r.stop.second - r.start.second);
}

int main() {
  Rectangle<intmax_t> r(0, 0, 1, 1);
  cout << area(r) << endl;  // This should output 1.
}
