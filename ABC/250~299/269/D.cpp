#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vd = vector<double>;
using vll = vector<long long>;
using vb = vector<bool>;
using vvb = vector<vb>;
using vvi = vector<vi>;
using vvll = vector<vll>;
using vs = vector<string>;
using vpii = vector<pair<int, int>>;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define all(obj) (obj).begin(), (obj).end()
#define rall(obj) (obj).rbegin(), (obj).rend()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)
#define debug(obj) for (auto x : obj) {cout << x << ' ';} cout << endl
ll gcd(ll x, ll y) { return (x % y)? gcd(y, x % y): y; }
ll lcm(ll x, ll y) { return x / gcd(x, y) * y; }

vvb seen, field;

void dfs(int i, int j) {
    seen[i][j] = true;
    vi dx = {-1, -1, 0, 0, 1, 1}, dy = {-1, 0, -1, 1, 0, 1};
    rep(dir, 6) {
        int x = i + dx[dir];
        int y = j + dy[dir];
        if ((x > 2000) || (x < 0) || (y > 2000) || (y < 0)) continue;
        if (field[x][y] == false) continue;
        if (seen[x][y]) continue;
        dfs(x, y);
    }
}

int main() {
    int N;
    cin >> N;
    vi X(N), Y(N);
    rep(i, N) cin >> X[i] >> Y[i];
    int count = 0;
    seen.assign(2001, vb(2001, false));
    field.assign(2001, vb(2001, false));
    rep(i, N) field[X[i] + 1000][Y[i] + 1000] = true;
    rep(i, 2001) rep(j, 2001) {
        if (seen[i][j]) continue;
        if (field[i][j] == false) continue;
        dfs(i, j);
        count++;
    }
    cout << count << endl;
    return 0;
}
