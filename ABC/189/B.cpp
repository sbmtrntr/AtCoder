#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, X, V, P = 0, Y = 0;
    cin >> N >> X;
    X *= 100;
    for (int i = 0; i < N; i++) {
        cin >> V >> P;
        Y += V * P;
        if (Y > X) {
            cout << i+1 << endl;
            return 0;
        }
    }
    cout << -1 << endl;
    return 0;
}