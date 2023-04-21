#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, B, ans;
    ans = 0;
    cin >> N >> A >> B;
    for (int i = 1; i <= N; i++) {
        string st_i = to_string(i);
        int sum = 0;
        for (int j = 0; j < st_i.size(); j++) {
            sum += int(st_i[j]-'0');
        }
        if (sum >= A && sum <= B) ans += i;
    }
    cout << ans << endl;
}