#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	vector<int> result;
    
    size_t last = 0;
    size_t next = 0;
    
    str += ",";
    while ((next = str.find(",", last)) != string::npos) {
        int i = stoi(str.substr(last, next-last));
        result.push_back(i);
        last = next + 1;
    }
    
    return result;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
