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
    
    int x;
    cin >> x;
    
    v.erase(std::begin(v) + x - 1);
    
    int a, b;
    cin >> a >> b;
    
    v.erase(std::begin(v) + a - 1, std::begin(v) + b - 1);
    
    cout << v.size() << endl;
    for (auto &&i : v) {
        cout << i << " ";
    }
    
    return 0;
}
