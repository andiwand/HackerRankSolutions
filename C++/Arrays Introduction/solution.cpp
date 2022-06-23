#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    vector<int> v;
    
    cin >> n;
    
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        v.push_back(a);
    }
    
    for (auto i = v.rbegin(); i != v.rend(); ++i) {
        cout << *i << " ";
    }
    
    return 0;
}
