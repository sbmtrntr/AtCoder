#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int N; cin >> N;
    vector<int> S(N, 3);
    int l = 0, r = N-1, mid = (l + r) / 2;
    S[0] = 0;
    S[N-1] = 1;
    while (r - l > 1) {
        cout << "? " << mid+1 << endl;
        int num; cin >> num;
        S[mid] = num;
        if (abs(S[mid] - S[mid+1]) == 1) {
            cout << "! " << mid+1 << endl;
            return 0;
        }
        if (abs(S[mid-1] - S[mid]) == 1) {
            cout << "! " << mid << endl;
            return 0;
        }
        num == 1 ? r = mid : l = mid;
        mid = (l + r) / 2;
    }
    abs(S[mid] - S[mid+1]) == 1 ? cout << "! " << mid+1 << endl : cout << "! " << mid << endl;
    return 0;
}
