#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < N; i++)
using ll = long long;

int N, K, Q;
ll x, y, ans = 0;
vector<int> A(N);
multiset<int> X;
multiset<int> Y;

void balance() {
    while(X.size() < K) {
    }
}

void add(ll v) {

}

void erase(ll v) {

}

int main(){
    cin >> N >> K >> Q;
    rep(i, K) X.insert(0);
    rep(i, N - K) Y.insert(0);
    rep(i, Q) {
        cin >> x >> y;
        x--;
        add(y);
        erase(A[x]);
        A[x] = y;
        cout << ans << endl;
    }
    return 0;
}