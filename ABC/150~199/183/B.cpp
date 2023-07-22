#include <bits/stdc++.h>
using namespace std;

int main() {
    double Sx, Sy, Gx, Gy;
    cin >> Sx >> Sy >> Gx >> Gy;
    Gy *= -1;
    double a, b, ans;
    a = (Sy - Gy) / (Sx - Gx);
    b = Sy - a*Sx;
    ans = b / a * (-1.0);
    cout << fixed << setprecision(10) << ans << endl;
}