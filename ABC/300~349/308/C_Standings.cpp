#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < N; i++)
using ll = long long;
int main(){
    int N;
    cin >> N;
    vector<double> A(N), B(N);
    vector<pair<double, int>> ans;
    rep(i, N) cin >> A[i] >> B[i];
    long double score;
    rep(i, N) {
        score = A[i] / (A[i] + B[i]);
        ans.push_back({score, -(i+1)});
    }
    sort(ans.begin(), ans.end());
    rep(i, N) {
        cout << -ans[N-i-1].second << ' ';
    }
    return 0;
}