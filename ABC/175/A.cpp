#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvll = vector<vll>;
using vs = vector<string>;

#define pb push_back
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)

ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

int main() {
    string S;
    cin >> S;
    if (S[0] == 'R' && S[1] == 'R' && S[2] == 'R') cout << 3 << endl;
    else if ((S[0] == 'R' && S[1] == 'R') || (S[1] == 'R' && S[2] == 'R')) cout << 2 << endl;
    else if (S[0] == 'R' || S[1] == 'R' || S[2] == 'R') cout << 1 << endl;
    else cout << 0 << endl;
}