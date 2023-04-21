#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, t, x, y, x_now, y_now, t_now;
    cin >> N;
    bool flag = true;
    x_now = 0;
    y_now = 0;
    t_now = 0;
    for (int i = 0; i < N; i++) {
        cin >> t >> x >> y;
        int distance = abs(x-x_now) + abs(y-y_now);
        int diff_t = t - t_now;
        if (diff_t < distance) {
            flag = false;
            break;
        }
        if ((diff_t - distance) % 2 == 1){
            flag = false;
            break;
        }
        x_now = x;
        y_now = y;
        t_now = t;
    }
    if (flag) cout << "Yes" << endl;
    else cout << "No" << endl;
}