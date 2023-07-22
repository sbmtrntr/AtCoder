#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int N, X, P[100];
    cin >> N >> X;
    for (int i = 0; i < N; i++) cin >> P[i];
    for (int i = 0; i < N; i++) {
        if (P[i] == X) {
            cout << i + 1 << endl;
            return 0;
        }
    }
    return 0;
}