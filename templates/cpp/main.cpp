#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void load_data(std::vector<std::string> &data) {
    const std::string filename = "data.txt";
    std::ifstream file;
    file.open(filename);
    
    std::string line;
    while (getline(file, line)) data.push_back(line);
    
    file.close();
}

void solve1(std::vector<std::string> &data) {
    std::cout << "Solution 1: " << 0 << std::endl;
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