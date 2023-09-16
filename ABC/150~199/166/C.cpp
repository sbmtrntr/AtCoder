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
    int N, M;
    cin >> N >> M;
    vi H(N), ok(N, 1);
    rep(i, N) cin >> H[i];
    rep(i, M) {
        int a, b;
        cin >> a >> b;
        if (H[a-1] > H[b-1]) ok[b-1] = 0;
        else if (H[a-1] == H[b-1]) ok[a-1] = ok[b-1] = 0;
        else ok[a-1] = 0;
    }
    cout << accumulate(all(ok), 0) << endl;
    return 0;
}
