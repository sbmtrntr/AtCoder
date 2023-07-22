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
#define all(obj) (obj).begin(), (obj).end()
#define rall(obj) (obj).rbegin(), (obj).rend()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define debug(vec) for (auto x : vec) cout << x << ' '
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }
 
int main() {
    ll N, P, Q, R;
    cin >> N >> P >> Q >> R;
    vll A(N), accum(N + 1);
    rep(i, N) cin >> A[i];
    rep(i, N) accum[i+1] = accum[i] + A[i];
    set<ll> st;
    rep(i, N+1) st.insert(accum[i]);
    for(auto x : st) {
        if (st.find(x + P) != st.end() && st.find(x + P + Q) != st.end() && st.find(x + P + Q + R) != st.end()){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}
