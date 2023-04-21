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
    ll N, P, Q, R;
    cin >> N >> P >> Q >> R;
    vll A(N), accum(N+1);
    accum[0] = 0;
    rep(i, N) {
        cin >> A[i];
        accum[i+1] = accum[i] + A[i];
    }
    return 0;
}