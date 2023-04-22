#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int N; cin >> N;
    string S; cin >> S;
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        if (S[i] == '|') cnt++;
        if (S[i] == '*') {
            if (cnt == 1) {
                cout << "in" << endl;
                return 0;
            }
            else {
                cout << "out" << endl;
                return 0;
            }
        }
    }
    return 0;
}