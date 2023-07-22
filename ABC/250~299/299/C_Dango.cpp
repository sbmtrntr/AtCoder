#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int N; cin >> N;
    string S; cin >> S;
    int ans = 0, temp = 0;
    for (int i = 0; i < N; i++) {
        if (S[i] == 'o') {
            temp++;
        }
        else {
            ans = max(ans, temp);
            temp = 0;
        }
    }
    temp = 0;
    for (int i = 0; i < N; i++) {
        if (S[N-i-1] == 'o') {
            temp++;
        }
        else {
            ans = max(ans, temp);
            temp = 0;
        }
    }
    ans == 0 ? cout << -1 << endl : cout << ans << endl;
    return 0;
}