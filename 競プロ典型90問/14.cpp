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
    vi A(N), B(N);
    rep(i, N) cin >> A[i];
    rep(i, N) cin >> B[i];
    ll ans = 0;
    sort(all(A)), sort(all(B));
    rep(i, N) ans += abs(A[i] - B[i]);
    cout << ans << endl;
    return 0;
}