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
    int X, Y, Z;
    cin >> X >> Y >> Z;
    if (X < 0) {X *= -1; Y *= -1; Z *= -1;}
    if (Y < 0 || X < Y) {
        cout << X << endl;
        return 0;
    }
    if (Z < 0) {
        cout << 2*Z*-1 + X << endl;
        return 0;
    }
    else {
        if (Y < Z) {
            cout << -1 << endl;
            return 0;
        }
        else cout << X << endl;
    }
    return 0;
}
