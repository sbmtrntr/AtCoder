#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, ans = 0;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    for (int i = 0; i < N; i++) {
        int x = A[i];
        for (int j = i; j < N; j++) {
            x = min(x, A[j]);
            ans = max(ans, x*(j-i+1));
        }
    }
    cout << ans << endl;
    return 0;
}