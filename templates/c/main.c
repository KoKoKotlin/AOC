#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* load_data() {
    FILE* file_ptr = fopen("data.txt", "r");
    
    fseek(file_ptr, 0, SEEK_END);  
    int size = ftell(file_ptr);
    char *data = malloc(sizeof(char) * size);
    rewind(file_ptr);
    
    fread(data, sizeof(char), size, file_ptr);

    fclose(file_ptr);

    return data;
}

void solve1(char *data) {    
    printf("Solution 1: %d\n", 0);
}

void solve2(char *data) {
    printf("Solution 2: %d\n", 0);
}

int main() {
    char *data = load_data();
    solve1(data);
    solve2(data);    
    
    free(data);
    return 0;
}