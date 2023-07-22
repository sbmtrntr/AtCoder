#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define debug(obj) for (auto x : obj) {cout << x << ' ';} cout << endl
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

int main() {
    int H, W;
    cin >> H >> W;
    vector<vector<char>> C(H, vector<char>(W));
    rep(i, H) rep(j, W) cin >> C[i][j];
    vector<int> ans(W);
    rep(i, H) {
        rep(j, W) {
            if (C[i][j] == '#') ans[j]++;
        }
    }
    debug(ans);
    return 0;
}