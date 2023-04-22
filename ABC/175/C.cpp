#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvll = vector<vll>;
using vs = vector<string>;

#define pb push_back
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)

ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

int main() {
    ll X, K, D;
    cin >> X >> K >> D;
    if (X < 0) X *= -1;
    ll straight = min(K, X / D);
    K -= straight;
    X -= straight * D;
    if (K % 2 == 0) cout << X << endl;
    else cout << abs(X - D) << endl;
    return 0;
}