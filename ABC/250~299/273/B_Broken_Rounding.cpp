#include <iostream>
#include <vector>
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
    ll X, K;
    cin >> X >> K;
    vll A(16);
    A[0] = 1;
    rep(i, 15) A[i+1] = 10*A[i];
    rep(i, K) {
        X = (X + A[i+1] / 2) / A[i+1] * A[i+1];
    }
    cout << X << endl;
    return 0;
}
