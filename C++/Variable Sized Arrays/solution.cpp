#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

std::vector<int> read_array() {
    int n;
    cin >> n;
    std::vector<int> result;
    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        result.push_back(a);
    }
    return result;
}

int main() {
    int n;
    int q;
    
    cin >> n >> q;
    
    std::vector<std::vector<int>> v;
    for (int i = 0; i < n; ++i) {
        v.push_back(read_array());
    }
    
    for (int i = 0; i < q; ++i) {
        int a;
        int b;
        cin >> a >> b;
        cout << v[a][b] << endl;
    }
    
    return 0;
}
