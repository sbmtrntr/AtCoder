#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define pb push_back
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define rrep(i, n) for (ll i = n - 1; -1 < i; i--)
#define debug(obj) for (auto x : obj) {cout << x << ' ';} cout << endl
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

int main() {
    int N;
    cin >> N;
    set<string> st;
    rep(i, N) {
        string s;
        cin >> s;
        if (s[0] != 'H' && s[0] != 'D' && s[0] != 'C' && s[0] != 'S') {
            cout << "No" << endl;
            return 0;
        }
        if (s[1] != 'A' && s[1] != '2' && s[1] != '3' && s[1] != '4' && s[1] != '5' 
            && s[1] != '6' && s[1] != '7' && s[1] != '8' && s[1] != '9' && s[1] != 'T'
            && s[1] != 'J' && s[1] != 'Q' && s[1] != 'K') {
                cout << "No" << endl;
                return 0;
            }
        if (st.count(s)) {
            cout << "No" << endl;
            return 0;
        }
        st.insert(s);
    }
    cout << "Yes" << endl;
    return 0;
}