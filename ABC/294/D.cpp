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


int main(){
    ll N, Q, q, last = 1;
    cin >> N >> Q;
    set<ll> called;
    rep(i, Q) {
        cin >> q;
        if (q == 1) {
            called.insert(last);
            last++;
        }
        else if (q == 2) {
            int x;
            cin >> x;
            called.erase(x);
        }
        else {
            int ans = *called.begin();
            cout << ans << endl;
        }
    }
    return 0;
}