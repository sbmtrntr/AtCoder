#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> data(6);
    for (int i = 0; i < 5; i++) {
        cin >> data[i];
    }
    data[5] = -1;
    bool flag = false;
    for (int i = 0; i < 5; i++) {
        if (data[i] == data[i+1]){
            flag = true;
        }
    }
    flag ? cout << "YES" << endl : cout << "NO" << endl;
}