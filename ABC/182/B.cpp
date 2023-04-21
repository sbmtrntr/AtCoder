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
    int N, ans, mx_cnt = 0;
    cin >> N;
    vi A(N);
    rep(i, N) cin >> A[i];
    reps(k, 2, 1001) {
        int cnt = 0;
        rep(j, N) {
            if(A[j] % k == 0) cnt++;
        }
        if (mx_cnt < cnt) {
            mx_cnt = cnt;
            ans = k;
        } 
    }
    cout << ans << endl;
    return 0;
}