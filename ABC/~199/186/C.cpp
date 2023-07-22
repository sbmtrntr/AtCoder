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
    int N, ans = 0;
    cin >> N;
    rrep(i, N) {
        bool flag = true;
        string str_i = to_string(i);
        rep(j, str_i.size()) if (str_i[j] == '7') {
            flag = false;
        }
        stringstream str_oct;
        str_oct << oct << stoi(str_i);
        string s = str_oct.str();
        rep(j, s.size()) if (s[j] == '7') {
            flag = false;
        }
        if (flag) ans++;
    }
    cout << ans << endl;
    return 0;
}