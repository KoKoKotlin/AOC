#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void load_data(int **ints, int *ssize) {
    FILE* file_ptr = fopen("data.txt", "r");
    
    fseek(file_ptr, 0, SEEK_END);  
    int size = ftell(file_ptr);
    char *data = malloc(sizeof(char) * size);
    rewind(file_ptr);
    
    fread(data, sizeof(char), size, file_ptr);

    // get number count
    int count = 0;
    for (int i = 0; data[i]; count += (data[i] == '\n' ? 1 : 0), i++);

    *ints = malloc(sizeof(int) * count);
    *ssize = count;

    // parse strings to int
    char *current = data;
    char buf[10];
    int *current_int = *ints;
    while (current - data < size) {
        memset(buf, 0, 10);

        char *next = strchr(current, '\n');
        memcpy(buf, current, next - current);

        *(current_int++) = atoi(buf);

        current = next + 1;
    }

    fclose(file_ptr);
}

void solve1(int *data, int number_of_values) {
    // find min and count diff to prev
    int prev = 0;   // previous value starts with 0
    
    int diff1 = 0, diff3 = 0;
    for (int j = 0; j < number_of_values; j++) {
        int current_best = 0xFFFFFF; 
        for (int i = 0; i < number_of_values; i++) {
            int current = data[i];

            if (current > prev && current - 3 <= prev && current < current_best) current_best = current;
        }

        if (current_best - prev == 1) diff1++;
        else if (current_best - prev == 3) diff3++;
        
        prev = current_best;
    }

    diff3++; // last value is always 3 higher then previous one
    
    printf("Solution 1: %d\n", diff1 * diff3);
}

/* too slow
// condition: data is sorted
int solve2rec(int prev, int* next, int curr_size) {
    if (curr_size <= 0) return 0;

    if (next[0] - prev <= 3) {
        return solve2rec(next[0], next + 1, curr_size - 1) +
               solve2rec(next[0], next + 2, curr_size - 2) +
               solve2rec(next[0], next + 3, curr_size - 3);
    }

    return 0;
}
*/

int compare_int(const void* p1, const void* p2) {
    int *i1 = (int*)p1;
    int *i2 = (int*)p2;
    
    if      (*i1 < *i2)  return -1;
    else if (*i1 == *i2) return 0;
    else if (*i1 > *i2)  return 1;
}

void solve2(int *data, int number_of_values) {
    int max = 0;
    for (int i = 0; i < number_of_values; i++) if (data[i] > max) max = data[i];
        
    int len = number_of_values + 2;
    
    int new_data[len];
    memcpy(new_data, data, sizeof(int) * number_of_values);
    
    new_data[number_of_values] = 0;
    new_data[number_of_values + 1] = max + 3;
    
    qsort(new_data, len, sizeof(int), &compare_int);
    
    long long possibilities = 1;
    
    for (int i = 2; i < len; i++) possibilities *= (new_data[i] - new_data[i - 2] <= 3) ? 2 : 1;

    printf("Solution 2: %lld\n", possibilities);
}

int main() {
    int* ints;
    int size;
    load_data(&ints, &size);

    solve1(ints, size);
    solve2(ints, size);    
    
    free(ints);
    return 0;
}