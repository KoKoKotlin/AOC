#!/bin/sh

set -xe

kotlinc main.kt -include-runtime -d main.jar && java -jar main.jar && rm main.jar