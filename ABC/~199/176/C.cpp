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
    int N;
    cin >> N;
    vi A(N);
    rep(i, N) cin >> A[i];
    ll ans = 0;
    reps(i, 1, N) {
        if (A[i-1] > A[i]) {
            ans += A[i-1] - A[i];
            A[i] += A[i-1] - A[i];
        }
    }
    cout << ans << endl;
    return 0;
}