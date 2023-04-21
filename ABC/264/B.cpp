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
    int R, C;
    cin >> R >> C;
    if (R == 1 || R == 15 || C == 1 || C == 15) cout << "black" << endl;
    else if (R == 2 || R == 14 || C == 2 || C == 14) cout << "white" << endl;
    else if (R == 3 || R == 13 || C == 3 || C == 13) cout << "black" << endl;
    else if (R == 4 || R == 12 || C == 4 || C == 12) cout << "white" << endl;
    else if (R == 5 || R == 11 || C == 5 || C == 11) cout << "black" << endl;
    else if (R == 6 || R == 10 || C == 6 || C == 10) cout << "white" << endl;
    else if (R == 7 || R == 9 || C == 7 || C == 9) cout << "black" << endl;
    else cout << "white" << endl;
    return 0;
}