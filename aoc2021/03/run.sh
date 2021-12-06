#!/bin/sh

set -xe

rustc main.rs && ./main && rm main