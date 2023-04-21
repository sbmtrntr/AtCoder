#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Y;
    cin >> N >> Y;
    for (int i = 0; i <= 2000; i++) {
        for (int j = 0; j <= 2000; j++) {
            int k = N-i-j;
            if (k < 0) break;
            if (10000*i + 5000*j + 1000*k == Y){
                cout << i << ' ' << j << ' ' << k << endl;;
                return 0;
            }
        }
    }
    cout << -1 << ' ' << -1 << ' ' << -1 << endl;
}