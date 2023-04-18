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
    ll N;
    cin >> N;
    vector<ll> A(N), dp(2*N+1);
    rep(i, N) cin >> A[i];
    rep(i, N) {
        ll parent = A[i] - 1;
        dp[2*i + 1] = dp[parent] + 1;
        dp[2*i + 2] = dp[parent] + 1;
    }
    rep(i, 2*N+1) cout << dp[i] << endl;
    return 0;
}