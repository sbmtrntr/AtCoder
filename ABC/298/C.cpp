#include <bits/stdc++.h>
#include <sstream>
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

int main(){
    int N, Q, n, x, y;
    cin >> N >> Q;
    map<int, multiset<int>> box;
    map<int, set<int>> card;
    rep(i, Q) {
        cin >> n;
        if (n == 1) {
            cin >> x >> y;
            box[y].insert(x);
            card[x].insert(y);
        }
        else if (n == 2) {
            cin >> x;
            debug(box[x]);
        }
        else {
            cin >> x;
            debug(card[x]);
        }
    }
    return 0;
}