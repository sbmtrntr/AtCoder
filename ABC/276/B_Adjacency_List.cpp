#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define pb push_back
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define rrep(i, n) for (ll i = n - 1; -1 < i; i--)
#define debug(obj) for (auto x : obj) {cout << x << ' ';} cout << endl
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

int main() {
    int N, M;
    cin >> N >> M;
    vector<int> A(M), B(M);
    rep(i, M) cin >> A[i] >> B[i];
    vector<vector<int>> ans(N, vector<int>());
    rep(i, M) {
        ans[A[i]-1].pb(B[i]);
        ans[B[i]-1].pb(A[i]);
    }
    rep(i, N) {
        cout << ans[i].size() << ' ';
        sort(all(ans[i]));
        rep(j, ans[i].size()) {
            cout << ans[i][j] << ' ';
        }
        cout << endl;
    }
    return 0;
}