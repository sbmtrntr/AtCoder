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

ll N, K, L;
vi A(1<<18);

bool solve(ll M) {
    ll cnt = 0, pre = 0;
    rep(i, N) {
        if (A[i] - pre >= M && L - A[i] >= M) {
            cnt += 1;
            pre = A[i];
        }
    }
    if (cnt >= K) return true;
    return false;
}

int main() {
    cin >> N >> L >> K;
    rep(i, N) cin >> A[i];
    ll left = 0, right = L;
    while (right - left > 1) {
        ll mid = (left + right) / 2;
        if (solve(mid)) left = mid;
        else right = mid;
    }
    cout << left << endl;
    return 0;
}