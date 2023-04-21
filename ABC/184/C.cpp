#include <bits/stdc++.h>
using namespace std;

#pragma GCC target("avx")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")

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
    int r1, r2, c1, c2;
    cin >> r1 >> c1 >> r2 >> c2;
    if (c1 == c2 && r1 == r2) cout << 0 << endl;
    else if (r1 + c1 == r2 + c2 ||
    r1 - c1 == r2 - c2 ||
    abs(c1 - c2) + abs(r1 - r2) <= 3) cout << 1 << endl;
    else if ((r1 + c1 + r2 + c2) % 2 == 0 || 
    abs(c1 - c2) + abs(r1 - r2) <= 6 || 
    abs(c1 + r1 - c2 - r2) <= 3 ||
    abs(c1 - r1 - c2 + r2) <= 3) cout << 2 << endl;
    else cout << 3 << endl;
    return 0;
}