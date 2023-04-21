#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, ans;
    ans = 0;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    bool flag = true;
    while (true) {
        for (int num : A) {
            if (num % 2 != 0) flag = false;
        }
        if (!flag) break;
        for (int &num : A) num /= 2; 
        ans++;
    }
    cout << ans << endl;
}
