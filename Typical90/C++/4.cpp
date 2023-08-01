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
    int H, W;
    cin >> H >> W;
    vvi A(H, vi(W)), B(H, vi(W));
    vi row(H), column(W);
    rep(i, H) rep(j, W) cin >> A[i][j];
    rep(i, H) rep(j, W) {
        row[i] += A[i][j];
        column[j] += A[i][j];
    }
    rep(i, H) {
        rep(j, W) {
        if (j != W-1) cout << row[i] + column[j] - A[i][j] << ' ';
        else cout << row[i] + column[j] - A[i][j];
        }
        cout << endl;
    }
    return 0;
}