#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int sum = 0;
    
    int n;
    while (cin >> n) {
        sum += n;
    }
    
    cout << sum;
    
    return 0;
}
