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
    int H, W; 
    cin >> H >> W;
    vector<vector<char>> G(H, vector<char>(W));
    rep(i, H) rep(j, W) {
        cin >> G[i][j];
    }
    int x = 0, y = 0, cnt = 0;
    while (true) {
        if (G[x][y] == 'U' && x != 0) x--;
        else if (G[x][y] == 'D' && x != H-1) x++;
        else if (G[x][y] == 'L' && y != 0) y--;
        else if (G[x][y] == 'R' && y != W-1) y++;
        else break;
        cnt++;
        if (cnt > 1e7) {
            cout << -1 << endl;
            return 0;
        }
    }
    cout << x+1 << ' ' << y+1 << endl;
    return 0;
}