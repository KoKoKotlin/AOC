#!/bin/sh

set -xe

g++ -lm -std=c++17 -Ofast main.cpp && ./a.out && rm a.out 