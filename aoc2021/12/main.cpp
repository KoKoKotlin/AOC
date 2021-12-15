#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

void load_data(std::vector<std::string> &data) {
    const std::string filename = "data.txt";
    std::ifstream file;
    file.open(filename);
    
    std::string line;
    while (getline(file, line)) data.push_back(line);
    
    file.close();
}

typedef std::vector<std::string> path_t;
typedef std::map<std::string, path_t> graph_t;

void solve1(std::vector<std::string> &data) {
    graph_t graph;

    // constructing the graph
    for (auto &line : data) {
        size_t delimIdx = line.find('-');
        std::string pos1 = line.substr(0, delimIdx);
        std::string pos2 = line.substr(delimIdx + 1, line.length());

        graph[pos1].push_back(pos2);
        graph[pos2].push_back(pos1);
    }

    std::queue<path_t> current_paths;
    current_paths.push(path_t {"start"});
    std::vector<path_t> finished_paths;

    while (!current_paths.empty()) {
        path_t path = current_paths.front();
        std::string from = path.back();
        
        if (from.compare("end") == 0) {
            finished_paths.push_back(path);
            current_paths.pop();
            continue;
        }

        std::vector<std::string> destinations = graph.at(from);

        for (std::string &to: destinations) {
            if (islower(to.at(0)) && std::find(path.begin(), path.end(), to) != path.end()) continue;   // visiting small cave twice

            path_t newPath;
            std::copy(path.begin(), path.end(), std::back_inserter(newPath));
            newPath.push_back(to);

            current_paths.push(newPath);    
        }

        current_paths.pop();
    }
    

    std::cout << "Solution 1: " << finished_paths.size() << std::endl;
}

bool visitedSmallCaveTwice(const path_t path) {
    size_t smallCaveDoubles = 0;
    std::vector<std::string> alreadySeen;

    for (const std::string &point : path) {
        if (std::find(alreadySeen.begin(), alreadySeen.end(), point) != alreadySeen.end()) continue;

        if (islower(point.at(0)) && std::count(path.begin(), path.end(), point) >= 2) smallCaveDoubles++; 
    }

    return smallCaveDoubles > 0;
}

void solve2(std::vector<std::string> &data) {
    graph_t graph;

    // constructing the graph
    for (auto &line : data) {
        size_t delimIdx = line.find('-');
        std::string pos1 = line.substr(0, delimIdx);
        std::string pos2 = line.substr(delimIdx + 1, line.length());

        graph[pos1].push_back(pos2);
        graph[pos2].push_back(pos1);
    }

    std::queue<path_t> current_paths;
    current_paths.push(path_t {"start"});
    std::vector<path_t> finished_paths;

    while (!current_paths.empty()) {
        path_t path = current_paths.front();
        std::string from = path.back();
        
        if (from.compare("end") == 0) {
            finished_paths.push_back(path);
            current_paths.pop();
            continue;
        }

        std::vector<std::string> destinations = graph.at(from);

        for (std::string &to: destinations) {
            
            if (to.compare("start") == 0) continue;
            if (islower(to.at(0)) && std::find(path.begin(), path.end(), to) != path.end() && visitedSmallCaveTwice(path)) continue;   // visiting small cave three times or more

            path_t newPath;
            std::copy(path.begin(), path.end(), std::back_inserter(newPath));
            newPath.push_back(to);

            current_paths.push(newPath);    
        }

        current_paths.pop();
    }
    

    std::cout << "Solution 2: " << finished_paths.size() << std::endl;
} 

int main() {
    std::vector<std::string> data;
    load_data(data);
    solve1(data);
    solve2(data);
    return 0;
}