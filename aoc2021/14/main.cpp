#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

void load_data(std::vector<std::string> &data) {
    const std::string filename = "test.txt";
    std::ifstream file;
    file.open(filename);
    
    std::string line;
    while (getline(file, line)) data.push_back(line);
    
    file.close();
}

struct rule {
    std::string match;
    char insert;
};

void solve1(std::vector<std::string> &data) {

    std::vector<rule> rules;
    for (int i = 2; i < data.size(); i++) {
        const std::string &line = data.at(i);
        rules.push_back({line.substr(0, 2), line.back()});
    }

    std::string current = data[0];
    std::string next;
    
    int iteration = 0;
    while (iteration++ < 10) {
        next.clear();
        next.push_back(current.at(0));

        for (int i = 0; i < current.length() - 1; i++) {
            const std::string &symbol = current.substr(i, 2);

            for (const rule &r: rules) {
                if (r.match.compare(symbol) != 0) continue;
                next.push_back(r.insert); 
                break;
            }

            next.push_back(current.at(i + 1));
        }

        current.assign(next.c_str());
    }

    std::map<char, size_t> char_counter;
    for (const char c : current) char_counter[c]++;
    
    size_t max = 0;
    size_t min = current.length();
    for (auto &[key, value] : char_counter) {
        max = std::max(value, max);
        min = std::min(value, min);
    }

    std::cout << "Solution 1: " << max - min << std::endl;
}

void solve2(std::vector<std::string> &data) {
    std::cout << "Solution 2: " << 0 << std::endl;
} 

int main() {
    std::vector<std::string> data;
    load_data(data);
    solve1(data);
    solve2(data);
    return 0;
}