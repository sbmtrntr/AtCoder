#include <bits/stdc++.h>
using namespace std;

int main() {
  int N, A;
  cin >> N >> A;

  // ここにプログラムを追記
  for (int i = 1; i <= N; i++){
    string op;
    int B;
    cin >> op >> B;
    if(op == "+"){
        A += B;
        cout << i << ":" << A << endl;
    }
    else if(op == "-"){
        A -= B;
        cout << i << ":" << A << endl;
    }
    else if(op == "*"){
        A *= B;
        cout << i << ":" << A << endl;
    }
    else if(op == "/"){
        if (B != 0){
          A /= B;
          cout << i << ":" << A << endl;
        }
        else{
            cout << "error" << endl;
            break;
        } 
    }
  }
}
