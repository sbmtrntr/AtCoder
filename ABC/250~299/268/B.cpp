#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vd = vector<double>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvll = vector<vll>;
using vs = vector<string>;
using vpii = vector<pair<int, int>>;

#define pb push_back
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)

ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

int main() {
    set<int> st;
    rep(i, 5) {
        int a;
        cin >> a;
        st.insert(a);
    }
    cout << st.size() << endl;
    return 0;
}
