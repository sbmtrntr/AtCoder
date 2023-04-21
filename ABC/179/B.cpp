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
    int N; cin >> N;
    vvi D(N, vi(2));
    rep(i, N) rep(j, 2) cin >> D[i][j];
    rep(i, N-2) {
        if (D[i][0] == D[i][1] && D[i+1][0] == D[i+1][1] && D[i+2][0] == D[i+2][1]) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}