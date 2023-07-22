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
    vll X(N);
    rep(i, N) cin >> X[i];
    ll m = 0, y = 0, t = 0;
    rep(i, N) {
        m += abs(X[i]);
        y += powl(abs(X[i]), 2);
    }
    cout << m << endl;
    cout << fixed << setprecision(10) << powl(y, 0.5) << endl;

    rep(i, N) {
        t = max(t, abs(X[i]));
    }
    cout << t << endl;
    return 0;
}