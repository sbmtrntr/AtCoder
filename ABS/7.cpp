#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, Alice, Bob;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) cin >> A[i];
    Alice = 0;
    Bob = 0;
    sort(A.begin(), A.end());
    for (int i = N-1; i >= 0; i -= 2) {
        Alice += A[i];
    }
    for (int i = N-2; i >= 0; i -= 2) {
        Bob += A[i];
    }
    cout << Alice - Bob << endl;
}   