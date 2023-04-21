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
    int X, Y, N;
    cin >> X >> Y >> N;
    if (X*3 < Y) cout << X * N << endl;
    else {
        if (N % 3 == 0) cout << Y*(N/3) << endl;
        else cout << Y*(N/3) + X*(N%3) << endl;
    }
    return 0;
}