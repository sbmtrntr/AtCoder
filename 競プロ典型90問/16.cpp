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
    int N, A, B, C;
    ll ans = 10000;
    cin >> N >> A >> B >> C;
    rep(i, 10000) rep(j, 10000) {
            ll temp = A*i + B*j;
            if ((N - temp) % C != 0 || N - temp < 0) continue;
            int k = (N-temp) / C;
            ans = min(ans, i+j+k);
        }
    cout << ans << endl;
    return 0;
}