#!/bin/sh

set -x

cd build && rm -rf * && cmake .. && make VERBOSE=1 && otool -L libhelloext.so
install_name_tool -change libboost_python.dylib /prod/boost/1.48.0.4/lib/libboost_python.dylib libhelloext.so && otool -L libhelloext.so
python -c "import libhelloext"