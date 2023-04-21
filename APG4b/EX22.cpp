#include <bits/stdc++.h>
using namespace std;
using pii = pair<int, int>;

int main() {
    int N;
    cin >> N;
    vector<pii> p;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        p.push_back(make_pair(b, a));
    }
    sort(p.begin(), p.end());
    for (pair<int, int> x : p) { 
        int a, b;
        tie(b, a) = x;
        cout << a << ' ' << b << endl;
    }
}