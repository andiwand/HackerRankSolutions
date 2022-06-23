#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    cin >> n;
    
    vector<int> v(n);
    for (int i = 0; i < n; ++i) {
        cin >> v[i];
    }
    
    sort(std::begin(v), std::end(v));
    
    for (auto &&i : v) {
        cout << i << " ";
    }
    
    return 0;
}
