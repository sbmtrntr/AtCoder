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
    int N;
    cin >> N;
    vll A(N);
    rep(i, N) cin >> A[i];
    ll mod = 1e9 + 7, ans = 0;
    vll accum(N+1);
    accum[0] = 0;
    rep(i, N) accum[i+1] = accum[i] + A[i];
    rep(i, N) {
        ans += A[i] * ((accum[N] - accum[i+1]) % mod);
        ans %= mod;
    }
    cout << ans << endl;
    return 0;
}