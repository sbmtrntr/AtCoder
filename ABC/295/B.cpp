#include <bits/stdc++.h>
#include <sstream>
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
    ll R, C;
    cin >> R >> C;
    vector<vector<char>> B(R, vector<char>(C));
    rep(i, R) rep(j, C) cin >> B[i][j];
    rep(i, R) {
        rep(j, C) {
            if (B[i][j] == '.' || B[i][j] == '#') {
                continue;
            }
            else {
                rep(k, R) {
                    rep(l, C) {
                        ll num = B[i][j] - '0';
                        if (B[k][l] == '#' && abs(i - k) + abs(j - l) <= num && abs(i - k) + abs(j - l) != 0) {
                            B[k][l] = '.';
                        }
                    }
                }
                B[i][j] = '.';
            }
        }
    }
    rep(i, R) {
        rep(j, C) {
            cout << B[i][j];
        }
        cout << endl;
    }
    return 0;
}