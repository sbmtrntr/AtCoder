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
    int N, ans = 0;
    cin >> N;
    vi L(N);
    rep(i, N) cin >> L[i];
    rep(i, N-2) {
        reps(j, i+1, N-1) {
            reps(k, j+1, N) {
                if (L[i] !=  L[j] && L[j] != L[k] && L[i] != L[k] && L[i] < L[j] + L[k] && L[j] < L[i] + L[k] && L[k] < L[j] + L[i]) ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}