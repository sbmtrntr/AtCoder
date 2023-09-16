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
    ll N;
    cin >> N;
    set<ll> st;
    reps(i, 1, pow(N, 0.5)+1) if (N % i == 0) {
        st.insert(i);
    }
    ll ans = powl(10, 12);
    for (auto x : st) ans = min(ans, x + N / x - 2);
    cout << ans << endl;
    return 0;
}
