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
    ll N, Q;
    cin >> N;
    vll A(N);
    rep(i, N) cin >> A[i];
    cin >> Q;
    sort(all(A));
    vll B(Q);
    rep(i, Q) cin >> B[i];
    rep(i, Q) {
        ll left = 0, right = N-1;
        while (right - left > 1) {
            int mid = (left + right)/2;
            if (A[mid] < B[i]) left = mid;
            else right = mid;
        }
        ll ans = min(abs(A[left] - B[i]), abs(A[right] - B[i]));
        cout << ans << endl;
    }
    return 0;
}
