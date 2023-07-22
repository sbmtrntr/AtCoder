#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vd = vector<double>;
using vll = vector<long long>;
using vb = vector<bool>;
using vvb = vector<vb>;
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
    vb ok(3, false);
    int A, B;
    cin >> A >> B;
    if (A == 1 || B == 1) ok[0] = true;
    if (A == 2 || B == 2) ok[1] = true;
    if (A == 3 || B == 3) {
        ok[0] = true;
        ok[1] = true;
    }
    if (A == 4 || B == 4) ok[2] = true;
    if (A == 5 || B == 5) {
        ok[0] = true;
        ok[2] = true;
    }
    if (A == 6 || B == 6) {
        ok[1] = true;
        ok[2] = true;
    }
    if (A == 7 || B == 7) {
        ok[0] = true;
        ok[1] = true;
        ok[2] = true;
    }
    cout << ok[0] + ok[1]*2 + ok[2]*4 << endl;
    return 0;
}
