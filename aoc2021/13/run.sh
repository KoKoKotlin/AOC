#!/bin/sh

set -xe

g++ -lm main.cpp && ./a.out && rm a.out 