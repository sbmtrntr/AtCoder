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

int main() {
    int N; cin >> N;
    ll ans, mod = 1e9+7, temp1 = 1, temp2 = 1, temp3 = 1;
    rep(i, N) temp1 = temp1 * 10 % mod;
    rep(i, N) temp2 = temp2 * 9 % mod;
    rep(i, N) temp3 = temp3 * 8 % mod;
    ans = temp1 - 2*temp2 + temp3;
    ans %= mod;
    ans = (ans + mod) % mod;
    cout << ans << endl;
    return 0;
}