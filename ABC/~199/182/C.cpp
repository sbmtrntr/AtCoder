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
    string N;
    cin >> N;
    int k = N.size(), mod = 0, mod1 = 0, mod2 = 0;
    rep(i, k) {
        mod += (int)N[i];
        if ((int)N[i] % 3 == 1) mod1++;
        if ((int)N[i] % 3 == 2) mod2++;
    }
    if (mod % 3 == 0) cout << 0 << endl;
    else if (mod % 3 == 1) {
        if (mod1 != 0) {
            if (k != 1) cout << 1 << endl;
            else cout << -1 << endl;
        }
        else {
            if (k != 2) cout << 2 << endl;
            else cout << -1 << endl;
        }
    }
    else {
        if (mod2 != 0) {
            if (k != 1) cout << 1 << endl;
            else cout << -1 << endl;
        }
        else {
            if (k != 2) cout << 2 << endl;
            else cout << -1 << endl;
        }
    }
    return 0;
}