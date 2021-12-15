#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define EPOCHS 100
#define WIDTH  10
#define HEIGHT 10

void load_data(std::vector<std::string> &data) {
    const std::string filename = "data.txt";
    std::ifstream file;
    file.open(filename);
    
    std::string line;
    while (getline(file, line)) data.push_back(line);
    
    file.close();
}

struct Cell {
    unsigned int energy_level;
    bool has_flashed;

    void reset() {
        if (this->has_flashed) this->energy_level = 0;
        this->has_flashed = false;
    }

    bool can_flash() {
        return this->energy_level > 9 && !this->has_flashed;
    }

    void flash(std::vector<Cell> &grid, size_t x, size_t y) {
        this->has_flashed = true;

        for (int dy = -1; dy <= 1; dy++) {
            for (int dx = -1; dx <= 1; dx++) {
                size_t nx = x + dx;
                size_t ny = y + dy;

                if (nx < 0 || nx >= WIDTH || ny < 0 || ny >= HEIGHT) continue;
                grid[nx + ny * WIDTH].energy_level++;
            }
        }
    }
};

void solve1(std::vector<std::string> &data) {
    std::vector<Cell> grid;
    for (auto &line : data) 
        for (auto c : line) 
            grid.push_back(Cell {(unsigned int)(c - '0'), false});

    size_t x = 0;
    unsigned long long flashes = 0;
    while(x++ < EPOCHS) {

        // first increment
        for (size_t y = 0; y < HEIGHT; y++)
            for (size_t x = 0; x < WIDTH; x++) 
                grid[x + y * WIDTH].energy_level++;
        
        // flashes
        bool dirty = true;
        while (dirty) {
            dirty = false;

            for (size_t y = 0; y < HEIGHT; y++) {
                for (size_t x = 0; x < WIDTH; x++) {
                    Cell &current = grid[x + y * WIDTH];

                    if (current.can_flash()) {
                        dirty = true;
                        current.flash(grid, x, y);
                        flashes++;
                    }
                } 
            }
        }

        for (auto &cell : grid) cell.reset();
    }

    std::cout << "Solution 1: " << flashes << std::endl;
}

void solve2(std::vector<std::string> &data) {
    std::vector<Cell> grid;
    for (auto &line : data) 
        for (auto c : line) 
            grid.push_back(Cell {(unsigned int)(c - '0'), false});

    size_t x = 0;
    unsigned long long flashes = 0;
    while(true) {

        // first increment
        for (size_t y = 0; y < HEIGHT; y++)
            for (size_t x = 0; x < WIDTH; x++) 
                grid[x + y * WIDTH].energy_level++;
        
        // flashes
        bool dirty = true;
        while (dirty) {
            dirty = false;

            for (size_t y = 0; y < HEIGHT; y++) {
                for (size_t x = 0; x < WIDTH; x++) {
                    Cell &current = grid[x + y * WIDTH];

                    if (current.can_flash()) {
                        dirty = true;
                        current.flash(grid, x, y);
                        flashes++;
                    }
                } 
            }
        }

        for (auto &cell : grid) cell.reset();

        bool allZero = true;
        for (size_t y = 0; y < WIDTH; y++) {
            for (size_t x = 0; x < HEIGHT; x++) {
                allZero &= grid[x + y * WIDTH].energy_level == 0;
            }
        }

        if (allZero) { 
            std::cout << "Solution 2: " << x + 1 << std::endl;
            break;
        }

        x++;
    }
} 

int main() {
    std::vector<std::string> data;
    load_data(data);
    solve1(data);
    solve2(data);
    return 0;
}