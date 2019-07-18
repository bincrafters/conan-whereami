cmake_minimum_required(VERSION 3.4.3)
project(whereami C)

if(EXISTS "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
  include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
else()
  include(conanbuildinfo.cmake)
endif()
conan_basic_setup()

if (WIN32 AND BUILD_SHARED_LIBS)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif(WIN32 AND BUILD_SHARED_LIBS)

set(SOURCE_FILES source_subfolder/src/whereami.c)
set(HEADER_FILES source_subfolder/src/whereami.h)

add_library(${CMAKE_PROJECT_NAME} ${SOURCE_FILES} ${HEADER_FILES})
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC source_subfolder/src)
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY C_STANDARD 99)

install(TARGETS ${CMAKE_PROJECT_NAME}
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)

install(FILES ${HEADER_FILES} DESTINATION include)
