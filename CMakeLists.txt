cmake_minimum_required(VERSION 2.8.12)
project(cmake_wrapper)

if(EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
  include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
else()
  include(conanbuildinfo.cmake)
endif()
conan_basic_setup()

set(SOURCE source_subfolder/src/whereami.c source_subfolder/src/whereami.h)
add_library(whereami ${SOURCE})
target_include_directories(whereami PUBLIC source_subfolder/src)
target_compile_features(whereami PRIVATE c_std_99)
