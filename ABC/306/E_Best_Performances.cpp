#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < N; i++)
using ll = long long;
int main(){
    int N, K, Q, x, y;
    cin >> N >> K >> Q;
    vector<int> A(N);
    set<int> B;
    rep(i, K) B.insert(0);
    rep(i, Q) {
        cin >> x >> y;
        B.erase(A[x-1]);
        B.insert(y);
        A[x-1] = y;
    }
    return 0;
}