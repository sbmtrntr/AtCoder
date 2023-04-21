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

bool judge(string S) {
    int x = 0;
    rep(i, S.size()) {
        if(S[i] == '(') x++;
        else x--;
        if (x < 0) return false;
    }
    if (x == 0) return true;
    return false;
}

int main() {
    int N;
    cin >> N;
    if (N % 2 != 0) {
        return 0;
    }
    rep(b, 1 << N) {
        string S;
        rep(i, N) {
            if ((b & (1 << i)) == 0) S = '(' + S;
            else S = ')' + S;
        }
        if (judge(S)) cout << S << endl;
    }
    return 0;
}