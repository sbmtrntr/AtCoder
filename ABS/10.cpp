#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    reverse(S.begin(), S.end());
    int ind = 0;
    while (ind < S.size()){
        if (S.substr(ind, 5) == "maerd") ind += 5;
        else if (S.substr(ind, 7) == "remaerd") ind += 7;
        else if (S.substr(ind, 5) == "esare") ind += 5;
        else if (S.substr(ind, 6) == "resare") ind += 6;
        else {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
}