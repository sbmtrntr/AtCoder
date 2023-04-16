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
    int N;
    cin >> N;
    vector<int> P(N);
    rep(i, N) cin >> P[i];
    int cnt = 0;
    do {
        cnt++;
        if (cnt == 2) {
            debug(P);
            return 0;
        }
    } while(prev_permutation(all(P)));
    // なんやねんこの機能w
    return 0;
}