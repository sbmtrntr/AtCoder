#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, ans, now;
    cin >> N;
    ans = 1;
    vector<int> D(N);
    for (int i = 0; i < N; i++) cin >> D[i];
    sort(D.begin(), D.end());
    now = D[N-1];
    for (int i = N-2; i>= 0; i--) {
        if (now > D[i]) {
            ans ++;
            now = D[i];
        }
    }
    cout << ans << endl;
}