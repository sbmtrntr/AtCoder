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
    ll N;
    cin >> N;
    set<ll> ans;
    reps(i, 1, (ll)powl(N, 0.5) + 1) if (N % i == 0) ans.insert(i), ans.insert(N/i);
    for(auto a : ans) cout << a << endl;
    return 0;
}