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
    int N, Q;
    cin >> N;
    vi accum1(N+1), accum2(N+1);
    rep(i, N) {
        int c, p;
        cin >> c >> p;
        if (c == 1) {
            accum1[i+1] = accum1[i] + p;
            accum2[i+1] = accum2[i];
        }
        else {
            accum1[i+1] = accum1[i];
            accum2[i+1] = accum2[i] + p;
        }
    }
    cin >> Q;
    rep(i, Q) {
        int l, r;
        cin >> l >> r;
        cout << accum1[r] - accum1[l-1] << ' ' << accum2[r] - accum2[l-1] << endl;
    }
    return 0;
}