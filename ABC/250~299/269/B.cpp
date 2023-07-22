#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vd = vector<double>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvll = vector<vll>;
using vs = vector<string>;
using vpii = vector<pair<int, int>>;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define all(obj) (obj).begin(), (obj).end()
#define rall(obj) (obj).rbegin(), (obj).rend()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define debug(obj) for (auto x : obj) {cout << x << ' ';} cout << endl
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }
 
int main() {
    int a, b, c, d;
    vector<vector<char>> S(10, vector<char>(10));
    rep(i, 10) rep(j, 10) cin >> S[i][j];
    bool flag = false;
    rep(i, 10) {
        rep(j, 10) {
            if (S[i][j] == '#') {
                a = i + 1;
                c = j + 1;
                flag = true;
                break;
            }
        }
        if (flag) break;
    }
    rep(i, 10) {
        rep(j, 10) {
            if (S[i][j] == '#') {
                b = i + 1;
                d = j + 1;
            }
        }
    }
    cout << a << ' ' << b << endl;
    cout << c << ' ' << d << endl;;
    return 0;
}
