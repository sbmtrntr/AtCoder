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

int main() {
    string S, T;
    cin >> S >> T;
    int cnt = 0;
    rep(i, S.size()-T.size()+1) {
        int temp = 0;
        rep(j, T.size()) {
            if (S[i+j] == T[j]) temp++;
        }
        cnt = max(cnt, temp);
    }
    cout << T.size() - cnt << endl;
    return 0;
}