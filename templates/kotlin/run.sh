#!/bin/sh

set -xe

kotlinc main.kt -include-runtime -d main.jar && java -jar -Xmx20g main.jar && rm main.jar