#include <iostream>
#include <vector>

using namespace std;

const int MAXN = 7000;
int N, K;
int fact[MAXN+1];
vector<int> A;

int count_reverse_permutations(int L, int R) {
    int cnt = 0;
    for (int i = L-1; i < R; i++) {
        for (int j = i+1; j <= R; j++) {
            if (A[i] > A[j]) {
                cnt++;
            }
        }
    }
    return cnt;
}

vector<int> reverse_permutation(int L, int R, vector<int> perm) {
    for (int i = L-1, j = R-1; i < j; i++, j--) {
        swap(perm[i], perm[j]);
    }
    return perm;
}

int main() {
    cin >> N >> K;

    // generate permutation A
    A.resize(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    // generate factorials
    fact[0] = 1;
    for (int i = 1; i <= N; i++) {
        fact[i] = i * fact[i-1];
    }

    // determine digits of Kth permutation
    vector<int> P(N);
    vector<int> Q(N);
    for (int i = 0; i < N; i++) {
        P[i] = i;
        int digit = (K-1) / fact[N-1-i];
        Q[i] = digit;
        K -= digit * fact[N-1-i];
    }

    // generate Kth permutation
    vector<int> ans;
    for (int i = N-1; i >= 0; i--) {
        ans.push_back(A[P[Q[i]]+1]);
        P.erase(P.begin() + Q[i]);
    }

    // reverse subarrays and count permutations until Kth permutation is reached
    for (int L = 1; L <= N; L++) {
        for (int R = L; R <= N; R++) {
            int count = count_reverse_permutations(L, R);
            if (K > count) {
                K -= count;
            } else {
                ans = reverse_permutation(L, R, ans);
                break;
            }
        }
        if (K == 0) {
            break;
        }
    }

    // output Kth permutation
    for (int i = 0; i < N; i++) {
        cout << ans[i] << " ";
    }
    cout << endl;

    return 0;
}
