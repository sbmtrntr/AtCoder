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
    int N, M, T, nokori;
    cin >> N >> M >> T;
    nokori = N;
    vi A(M), B(M);
    rep (i, M) cin >> A[i] >> B[i];
    rep (i, M) {
        if (i == 0) nokori -= A[i];
        else nokori -= A[i] - B[i-1];
        if (nokori <= 0) {
            cout << "No" << endl;
            return 0;
        }
        nokori = min(N, nokori + (B[i] - A[i]));
    }
    if (nokori - (T - B[M-1]) > 0) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}