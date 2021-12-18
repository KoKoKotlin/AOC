#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <memory>

#define INFINITY INT32_MAX

void load_data(std::vector<std::string> &data) {
    const std::string filename = "data.txt";
    std::ifstream file;
    file.open(filename);
    
    std::string line;
    while (getline(file, line)) data.push_back(line);
    
    file.close();
}

struct point {
    size_t x, y;
    int cost;
    int distance = INFINITY;
    bool done = false;
    point *prev = nullptr;
};

std::vector<size_t> get_neighbors(size_t x, size_t y, size_t width, size_t height) {
    std::vector<size_t> neighbors;

    if (x >= 1)         neighbors.push_back(x - 1 + y * width);
    if (x + 1 < width)  neighbors.push_back(x + 1 + y * width);
    if (y >= 1)         neighbors.push_back(x + (y - 1) * width);
    if (y + 1 < height) neighbors.push_back(x + (y + 1) * width);
    
    return neighbors;
}

void solve1(std::vector<std::string> &data) {
    
    // load the points
    size_t width = data.at(0).length(), height = data.size();
    std::vector<point> points(width * height);
    for (size_t y = 0; y < height; y++) {
        for (size_t x = 0; x < width; x++) {
            int cost = (int)(data.at(y).at(x) - '0');
            points[x + y * width].x = x;
            points[x + y * width].y = y;
            points[x + y * width].cost = cost;
        }
    }

    std::list<std::reference_wrapper<point>> pending;
    points[0].distance = 0;
    pending.push_back(points[0]);

    while (!pending.empty()) {
        int maxDist = INT32_MAX;
        point *max = nullptr;
        
        // find point with least distance
        for (point &p : pending) {
            if (maxDist > p.distance) {
                maxDist = p.distance;
                max = &p;
            }
        }

        // remove that point
        pending.remove_if([&](std::reference_wrapper<point> &p) {
            return p.get().x == max->x && p.get().y == max->y;
        });

        // if the end is reached exit
        if (max->x == width - 1 && max->y == height - 1) break;
        
        // if the point is already done continue with the next one
        if (max->done) continue;

        max->done = true;
        std::vector<size_t> neighbors = get_neighbors(max->x, max->y, width, height);

        // update each neighbor
        for (size_t &idx : neighbors) {
            point &n = points.at(idx);

            if (n.distance > n.cost + max->distance) {
                n.distance = n.cost + max->distance;
                n.prev = max;
            }

            // add the neighbor to the pending list, if he is not already contained
            bool isContained = false;
            for (auto &p : pending) {
                if (p.get().x == n.x && p.get().y == n.y) {
                    isContained = true;
                    break;
                }
            }

            if (!isContained) pending.push_back(n);
        }
    }

    std::cout << "Solution 1: " << points.back().distance << std::endl;
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