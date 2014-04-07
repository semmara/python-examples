#!/bin/sh

set -x

cd build && rm -rf * && cmake .. && make VERBOSE=1 && otool -L libmensch.so
python -c "import libmensch"

