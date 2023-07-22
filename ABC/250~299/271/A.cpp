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
using Graph = vll;
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
    int N;
    cin >> N;
    if (N == 0) {
        cout << "00" << endl;
        return 0;
    }
    string S = "0123456789ABCDEF", ans;
    while (N > 0) {
        ans += S[N % 16];
        N /= 16;
    }
    if (ans.size() == 1) ans = ans + "0";
    cout << ans[1] << ans[0] << endl;
    return 0;
}
