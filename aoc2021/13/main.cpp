#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <array>

void load_data(std::vector<std::string> &data) {
    const std::string filename = "data.txt";
    std::ifstream file;
    file.open(filename);
    
    std::string line;
    while (getline(file, line)) data.push_back(line);
    
    file.close();
}

struct point {
    int x;
    int y;
};

#define X_AXIS 0
#define Y_AXIS 1

struct fold {
    int value;
    int axis; // 0 == x, 1 == y
};

void print_points(const std::vector<point> points) {
    for (const auto &point : points) std::cout << point.x << " " << point.y << std::endl;
    std::cout << std::endl;
}

void do_folds(const fold &f, std::vector<point> &points) {
    for (auto &point: points) {
        if (f.axis == X_AXIS) {
            if (point.x >= f.value) point.x = 2 * f.value - point.x;
        } else {
            if (point.y >= f.value) point.y = 2 * f.value - point.y;
        }
    }

    std::sort(points.begin(), points.end(), [](const point &a, const point &b) {
        if (a.x != b.x) return a.x > b.x;
        else return a.y > b.y;
    });

    auto iter = std::unique(points.begin(), points.end(), [](const point &a, const point &b) {
        return a.x == b.x && a.y == b.y;
    });
    
    points.erase(iter, points.end());
}

void solve1(std::vector<std::string> &data) {

    // load points
    size_t idx = 0;
    std::vector<point> points;
    while (true) {
        std::string line = data[idx];
        
        if (line.find_first_not_of (' ') == line.npos) break;     // line was only whitespace

        size_t delimIdx = line.find(',');

        int x = std::stoi(line.substr(0, delimIdx));
        int y = std::stoi(line.substr(delimIdx + 1, line.size()));
        
        points.push_back({x, y});
        
        idx++;
    }

    // load folds
    idx++;
    std::vector<fold> folds;
    for (; idx < data.size(); idx++) {
        std::string line = data[idx];

        size_t delimIdx = line.find("=");
        int value = std::stoi(line.substr(delimIdx + 1, line.size()));
        folds.push_back({value, (line.find('x') != line.npos) ? X_AXIS : Y_AXIS});
    }

    do_folds(folds[0], points);
    
    std::cout << "Solution 1: " << points.size() << std::endl;
}

void solve2(std::vector<std::string> &data) {

    // load points
    size_t idx = 0;
    std::vector<point> points;
    while (true) {
        std::string line = data[idx];
        
        if (line.find_first_not_of (' ') == line.npos) break;     // line was only whitespace

        size_t delimIdx = line.find(',');

        int x = std::stoi(line.substr(0, delimIdx));
        int y = std::stoi(line.substr(delimIdx + 1, line.size()));
        
        points.push_back({x, y});
        
        idx++;
    }

    // load folds
    idx++;
    std::vector<fold> folds;
    for (; idx < data.size(); idx++) {
        std::string line = data[idx];

        size_t delimIdx = line.find("=");
        int value = std::stoi(line.substr(delimIdx + 1, line.size()));
        folds.push_back({value, (line.find('x') != line.npos) ? X_AXIS : Y_AXIS});
    }
    
    for (const auto &fold : folds) 
        do_folds(fold, points);
    
    const int width = 40; /*std::max(points, [](const point &a, const point &b) {
        return a.x > b.x;
    });*/
    
    std::array<char, width * 10> outputbuf;

    outputbuf.fill(' ');

    for (const auto &point : points) {
        outputbuf[point.x + point.y * width] = '*';
    }
    
    print_points(points);

    std::cout << "Solution 2: " << "Read the letters below" << std::endl;

    for (size_t y = 0; y < 10; y++) {
        for (size_t x = 0; x < width; x++) {
            std::cout << outputbuf[x + y * width];
        }
        std::cout << std::endl;
    }
}

int main() {
    std::vector<std::string> data;
    load_data(data);
    solve1(data);
    solve2(data);
    return 0;
}