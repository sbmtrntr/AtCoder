#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vd = vector<double>;
using vll = vector<long long>;
using vb = vector<bool>;
using vvb = vector<vb>;
using vvi = vector<vi>;
using vvll = vector<vll>;
using vs = vector<string>;
using vpii = vector<pair<int, int>>;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define all(obj) (obj).begin(), (obj).end()
#define rall(obj) (obj).rbegin(), (obj).rend()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define debug(obj) for (auto x : obj) {cout << x << ' ';} cout << endl
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

int main() {
    int N, M;
    cin >> N >> M;
    vvll ans(N, vll(N));
    rep(i, M) {
        int k;
        cin >> k;
        vll temp(k);
        rep(j, k) cin >> temp[j];
        rep(j, k-1) reps(l, j+1, k) ans[temp[j]-1][temp[l]-1] = ans[temp[l]-1][temp[j]-1] = 1;
    }
    rep(i, N) {
        int temp = 0;
        rep(j, N) temp += ans[i][j];
        if (temp != N-1) {
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}
