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
    int N;
    cin >> N;
    vi x(N), y(N);
    rep(i, N) cin >> x[i] >> y[i];
    rep(i, N-2) reps(j, i+1, N-1) reps(k, j+1, N){
        int x1, x2, y1, y2;
        x1 = x[j] - x[i];
        x2 = x[k] - x[i];
        y1 = y[j] - y[i];
        y2 = y[k] - y[i];
        if (x1 * y2 == x2 * y1) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}