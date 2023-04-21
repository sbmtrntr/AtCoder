#include <iostream>
using namespace std;

int X, Y;
int main() {
    cin >> X >> Y;
    if ((X > Y && X - Y < 3) || (X < Y && Y - X < 3)){
        cout << "Yes" << endl;
    }
    else{
        cout << "No" << endl;
    }
}