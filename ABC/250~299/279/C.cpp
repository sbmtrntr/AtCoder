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
    int H, W;
    cin >> H >> W;
    vector<string> S(H), T(H), S_retu(W), T_retu(W);
    rep(i, H) cin >> S[i];
    rep(i, H) cin >> T[i];
    rep(i, H) {
        rep(j, W) {
            S_retu[j] += S[i][j];
            T_retu[j] += T[i][j];
        }
    }
    map<string, int> mp;
    rep(i, W) {
        mp[S_retu[i]] += 1;
    }
    rep(i, W) {
        mp[T_retu[i]] -= 1;
    }
    for (auto x : mp) {
        if (x.second != 0) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}