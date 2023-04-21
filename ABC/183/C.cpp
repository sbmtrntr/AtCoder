#include <bits/stdc++.h>
using namespace std;

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
    int N, K, ans = 0;
    cin >> N >> K;
    vvi T(N, vi(N));
    rep(i, N) rep(j, N) cin >> T[i][j];
    vi index;
    rep(i, N) index.pb(i);
    do {
        int time = 0;
        rep(i, N) time += T[index[i]][index[i+1%N]];
        if (time == K) ans++;
    } while(next_permutation(index.begin()+1, index.end()));
    cout << ans << endl;
    return 0;    
}