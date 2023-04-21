#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    int key;
    map<int, int> A;
    for (int i = 0; i < N; i++) {
        cin >> key;
        if (A.count(key)) A[key]++;
        else A[key] = 1;
    }
    int mx = 0;
    int max_key = 0;
    for (auto p : A) { 
        if (mx < p.second) {
            mx = p.second;
            max_key = p.first;
        }
    }
    cout << max_key << " " << mx << endl;
}