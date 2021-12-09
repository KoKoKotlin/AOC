#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <queue>

#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define SENTINEL 0xFFFFFFFF

void load_data(std::vector<std::string> &data) {
    const std::string filename = "data.txt";
    std::ifstream file;
    file.open(filename);
    
    std::string line;
    while (getline(file, line)) data.push_back(line);
    
    file.close();
}

size_t convertXY(std::size_t width, std::size_t x_, std::size_t y_) { 
    return x_ + y_ * width; 
}

int getMinNeighbor(std::vector<int> &vals, std::size_t x, std::size_t y, std::size_t width, std::size_t height) {
    int min = INT32_MAX;


    if (x > 0)
        min = MIN(min, vals[convertXY(width, x - 1, y)]);
    if (x < width - 1)
        min = MIN(min, vals[convertXY(width, x + 1, y)]);
    if (y > 0)
        min = MIN(min, vals[convertXY(width, x, y - 1)]);
    if (y < height - 1)
        min = MIN(min, vals[convertXY(width, x, y + 1)]);

    return min;
}

void solve1(std::vector<std::string> &data) {
    std::vector<int> vals;
    const std::size_t width  = data[0].length();
    const std::size_t heigth = data.size();
    
    for (std::string &str : data) {
        for (char c : str) {
            vals.push_back((int)c - 48);
        }
    }

    std::vector<int> minVals;
    for (size_t y = 0; y < heigth; y++) {
        for (size_t x = 0; x < width; x++) {
            int val = vals[x + y * width];

            if (val < getMinNeighbor(vals, x, y, width, heigth)) {
                minVals.push_back(val);
            }
        }
    }


    std::for_each(minVals.begin(), minVals.end(), [](int &i){ ++i; });
    int sum = std::accumulate(minVals.begin(), minVals.end(), 0);

    std::cout << "Solution 1: " << sum << std::endl;
}

std::size_t getBasinSize(std::vector<int> &vals, std::size_t index, std::size_t width, std::size_t height) {
    std::set<std::size_t> basin;
    std::queue<std::size_t> toCheck;

    toCheck.push(index);

    while (!toCheck.empty()) {
        std::size_t next = toCheck.front();
        basin.insert(next);

        size_t x = next % width;
        size_t y = next / width;
        
        size_t neighbors[] = { SENTINEL, SENTINEL, SENTINEL, SENTINEL };  

        if (x > 0)
            neighbors[0] = convertXY(width, x - 1, y);
        if (x < width - 1)
            neighbors[1] = convertXY(width, x + 1, y);
        if (y > 0)
            neighbors[2] = convertXY(width, x, y - 1);
        if (y < height - 1)
            neighbors[3] = convertXY(width, x, y + 1);

        for (size_t i = 0; i < 4; i++) {
            if (neighbors[i] == SENTINEL) continue;
            int val = vals[neighbors[i]];

            if (val == 9 || basin.find(neighbors[i]) != basin.end()) continue;
            toCheck.push(neighbors[i]);
        }

        toCheck.pop();
    }

    return basin.size();
}

void solve2(std::vector<std::string> &data) {
        std::vector<int> vals;
    const std::size_t width  = data[0].length();
    const std::size_t heigth = data.size();
    
    for (std::string &str : data) {
        for (char c : str) {
            vals.push_back((int)c - 48);
        }
    }

    std::vector<std::size_t> basinSize;
    for (size_t y = 0; y < heigth; y++) {
        for (size_t x = 0; x < width; x++) {
            int val = vals[x + y * width];

            if (val < getMinNeighbor(vals, x, y, width, heigth)) {
                basinSize.push_back(getBasinSize(vals, x + y * width, width, heigth));
            }
        }
    }

    std::sort(basinSize.begin(), basinSize.end(), std::greater<>());
    std::cout << "Solution 2: " << basinSize[0] * basinSize[1] * basinSize[2] << std::endl;
} 

int main() {
    std::vector<std::string> data;
    load_data(data);
    solve1(data);
    solve2(data);
    return 0;
}