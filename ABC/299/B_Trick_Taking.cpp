#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int N, T, num = 0, ans = 0; cin >> N >> T;
    vector<int> C(N), R(N);
    for(int i = 0; i < N; i++) cin >> C[i];
    for(int i = 0; i < N; i++) cin >> R[i];
    bool flag = false;
    for (int i = 0; i < N; i++) {
        if (C[i] == T) {
            flag = true;
        }
    }
    if (flag) {
        for (int i = 0; i < N; i++) {
            if (C[i] == T && R[i] > num) {
                ans = i+1;
                num = R[i];
            }
        }
    }
    else {
        for (int i = 0; i < N; i++) {
            if (C[i] == C[0] && R[i] > num) {
                ans = i+1;
                num = R[i];
            }
        }
    }
    cout << ans << endl;
    return 0;
}