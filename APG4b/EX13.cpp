#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int mean = 0;
    vector<int> vec(N);
    for (int i = 0; i < N; i++){
        cin >> vec[i];
        mean += vec[i];
    }
    mean /= N;
    int ans;
    for (int i = 0; i < N; i++){
        ans = mean - vec[i];
        if (ans > 0) {
            cout << ans << endl;
        }
        else {
            cout << ans*(-1) << endl;
        }
    }
}
