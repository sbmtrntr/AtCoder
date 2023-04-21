#include <bits/stdc++.h>
using namespace std;

#pragma GCC target("avx")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

using ull = unsigned long long;
using ll = long long;
using vi = vector<int>;
using vl = vector<long>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvl = vector<vl>;
using vvll = vector<vll>;
using vs = vector<string>;
using pii = pair<int, int>;

#define pb push_back
#define mp make_pair
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define rrep(i, n) reps(i, 1, n + 1)
#define repd(i,n) for(ll i=n-1;i>=0;i--)
#define rrepd(i,n) for(ll i=n;i>=1;i--)

int main() {
    ll H1, H2, W1, W2;
    cin >> H1 >> W1;
    vvll A(H1, vll(W1));
    rep(i, H1) rep(j, W1) cin >> A[i][j];
    cin >> H2 >> W2;
    vvll B(H2, vll(W2)), C(H2, vll(W2));
    rep(i, H2) rep(j, W2) cin >> B[i][j];

    rep(i, 1 << H1) rep(j, 1 << W1){
        int H3 = 0;
        rep(k, H1) if((i & (1 << k))) H3++;
        int W3 = 0;
        rep(k, W1) if((j & (1 << k))) W3++;
        if (H3 != H2 || W2 != W2) continue;

        int cy = 0;
        rep(y, H1) if (i & (1 << y)) {
            int cx = 0;
            rep(x, W1) if (j & (1 << x)) {
                C[cy][cx] = A[y][x];
                cx++;
            }
            cy++;
        }
        bool match = true;
        rep(x, H2) rep(y, W2) {
            if (C[y][x] != B[y][x]) match = false;
        }
        if (match) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}
