#!/bin/bash

set -xe

gcc -lm main.c && ./a.out && rm a.out