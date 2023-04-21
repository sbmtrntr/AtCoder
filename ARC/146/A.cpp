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
    int N;
    cin >> N;
    vs A(N);
    rep(i, N) cin >> A[i];
    sort(all(A));
    string ans;
    cout << max({A[N-1] + A[N-2] + A[N-3], A[N-1] + A[N-3] + A[N-2], 
                 A[N-2] + A[N-1] + A[N-3], A[N-2] + A[N-3] + A[N-1], 
                 A[N-3] + A[N-1] + A[N-2], A[N-3] + A[N-2] + A[N-1]}) << endl;
    return 0;
}
