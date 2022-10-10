#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);


std::vector<std::vector<int>> floyd(int road_nodes, int road_edges, const vector<int> &road_from, const vector<int> &road_to, const vector<int> &road_weight) {
    static constexpr int inf = -1;

    std::vector<std::vector<int>> result(road_nodes);
    for (int i = 0; i < road_nodes; ++i) {
        result[i] = std::vector<int>(road_nodes, inf);
        result[i][i] = 0;
    }
    for (int i = 0; i < road_edges; ++i) {
        result[road_from[i]][road_to[i]] = road_weight[i];
    }
    
    for (int k = 0; k < road_nodes; ++k) {
        for (int i = 0; i < road_nodes; ++i) {
            for (int j = 0; j < road_nodes; ++j) {
                if (result[i][k] == inf || result[k][j] == inf) {
                    continue;
                }
                int alt = result[i][k] + result[k][j];
                if (result[i][j] == inf) {
                    result[i][j] = alt;
                } else {
                    result[i][j] = std::min(result[i][j], alt);
                }
            }
        }
    }

    return result;
}


int main()
{
    string road_nodes_edges_temp;
    getline(cin, road_nodes_edges_temp);

    vector<string> road_nodes_edges = split(rtrim(road_nodes_edges_temp));

    int road_nodes = stoi(road_nodes_edges[0]);
    int road_edges = stoi(road_nodes_edges[1]);

    vector<int> road_from(road_edges);
    vector<int> road_to(road_edges);
    vector<int> road_weight(road_edges);

    for (int i = 0; i < road_edges; i++) {
        string road_from_to_weight_temp;
        getline(cin, road_from_to_weight_temp);

        vector<string> road_from_to_weight = split(rtrim(road_from_to_weight_temp));

        int road_from_temp = stoi(road_from_to_weight[0]);
        int road_to_temp = stoi(road_from_to_weight[1]);
        int road_weight_temp = stoi(road_from_to_weight[2]);

        road_from[i] = road_from_temp-1;
        road_to[i] = road_to_temp-1;
        road_weight[i] = road_weight_temp;
    }
    
    auto sol = floyd(road_nodes, road_edges, road_from, road_to, road_weight);

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string first_multiple_input_temp;
        getline(cin, first_multiple_input_temp);

        vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

        int x = stoi(first_multiple_input[0])-1;
        int y = stoi(first_multiple_input[1])-1;
        
        std::cout << sol[x][y] << "\n";
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
