#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vll = vector<long long>;
using vvi = vector<vi>;
using vvll = vector<vll>;
using vs = vector<string>;

#define pb push_back
#define all(obj) (obj).begin(), (obj).end()
#define reps(i, a, n) for (ll i = (a); i < (ll)(n); ++i)
#define rep(i, n) reps(i, 0, n)

int main() {
    vi x(4), y(4);
	rep(i,4) cin >> x[i] >> y[i];
	
	rep(i,4) {
		int a = i;
		int b = (i+1)%4;
		int c = (i+2)%4;
		
		int x1 = x[b]-x[a], y1 = y[b]-y[a], x2 = x[c]-x[b], y2 = y[c]-y[b];
		if(x1*y2 - x2*y1 <= 0){
			cout << "No" << endl;
			return 0;
		}
	}
	cout << "Yes" << endl;

    return 0;
}