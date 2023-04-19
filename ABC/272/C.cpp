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
    int N;
    cin >> N;
    vll A(N);
    rep(i, N) cin >> A[i];
    sort(all(A));
    vi odd(2), even(2);
    rep(i, N) {
        if (A[i] % 2) odd.pb(A[i]);
        else even.pb(A[i]);
    }
    if (odd.size() < 4 && even.size() < 4) {
        cout << -1 << endl;
    }
    else {
        cout << max(odd[odd.size()-1] + odd[odd.size()-2], even[even.size()-1] + even[even.size()-2]) << endl;
    }
    return 0;
}
