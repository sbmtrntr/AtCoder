#include <iostream>
using namespace std;

int N, H[100], ans = -1, highest = 0;
int main() {
    cin >> N;
    for (int i = 0; i < N; i++) cin >> H[i];
    for (int i = 0; i < N; i++) {
        if (highest < H[i]) {
            ans = i+1;
            highest = H[i];
        }
    }
    cout << ans << endl;
}
