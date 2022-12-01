#!/bin/sh

set -xe

g++ -lm main.cpp -std=c++17 && ./a.out && rm a.out 