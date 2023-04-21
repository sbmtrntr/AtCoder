#include <iostream>
#include <vector>
using namespace std;

int N;

int main() {
    cin >> N;
    int A[N];
    int B[N];
    for (int i = 0; i < N; i++){
        cin >> A[i];
    }
    for (int i = 0; i < N; i++){
        cin >> B[i];
    }
    int ans = 0;
    for (int i = 0; i < N; i++){
        ans += A[i]*B[i];
    }
    if (ans == 0){
        cout << "Yes" << endl;
    }
    else { 
        cout << "No" << endl;
    }
}