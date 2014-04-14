cmake_minimum_required (VERSION 2.6)
#project (helloext)


SET(LIBNAME "mensch" CACHE STRING "name of the plugin python wrapper or empty for no plugin")
SET(LIB_FOO "foo" CACHE STRING "name of the lib foo")

#SET(PLUGIN_TYPE "SHARED") # .dylib on osx
SET(PLUGIN_TYPE "MODULE") # .so on osx (Python can only handle *.so)
SET(BOOST_VERSION "1.55.0-local" CACHE STRING "used boost version")
SET(PROD "/prod" CACHE STRING "prod dir")

MESSAGE(STATUS "-----------------------------------------")

# python include dir
FIND_PATH(PYTHON_INCLUDE_DIR
  Python.h
  /usr/include/python2.7/
)
MESSAGE(STATUS "PYTHON_INCLUDE_DIR: ${PYTHON_INCLUDE_DIR}")

# python lib
FIND_LIBRARY(PYTHON_LIBRARY
  python2.7
  /System/Library/Frameworks/Python.framework/Versions/Current/lib
  /usr/lib/python2.7/config/
  /usr/lib
)
MESSAGE(STATUS "PYTHON_LIBRARY: ${PYTHON_LIBRARY}")

# boost include dir
FIND_PATH(BOOST_INCLUDE_DIR
  boost/python.hpp
  ${PROD}/boost/${BOOST_VERSION}/include/
)
MESSAGE(STATUS "BOOST_INCLUDE_DIR: ${BOOST_INCLUDE_DIR}")

# boost lib
FIND_LIBRARY(BOOST_LIBRARY
  libboost_python.a
  ${PROD}/boost/${BOOST_VERSION}/lib/
)
MESSAGE(STATUS "BOOST_LIBRARY: ${BOOST_LIBRARY}")

MESSAGE(STATUS "-----------------------------------------")


ADD_DEFINITIONS("-Wall -Wextra")

INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_DIR} ${PYTHON_LIBRARY} ${BOOST_INCLUDE_DIR})
ADD_LIBRARY(${LIBNAME} ${PLUGIN_TYPE} example.cpp )
TARGET_LINK_LIBRARIES(${LIBNAME} ${BOOST_LIBRARY} ${PYTHON_LIBRARY})

ADD_LIBRARY(${LIB_FOO} ${PLUGIN_TYPE} example2.cpp foo.c)
TARGET_LINK_LIBRARIES(${LIB_FOO} ${BOOST_LIBRARY} ${PYTHON_LIBRARY})

