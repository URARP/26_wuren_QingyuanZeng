cmake_minimum_required(VERSION 3.10)

project(Test)

set(CMAKE_CXX_STANDARD 14)

if(DEFINED ENV{OpenCV_DIR})
    set(OpenCV_DIR $ENV{OpenCV_DIR})
endif()

find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_subdirectory(common)
add_subdirectory(modules)

add_executable(test main.cpp)

target_include_directories(test PUBLIC 
    ${CMAKE_SOURCE_DIR}/modules/A1/include
    ${CMAKE_SOURCE_DIR}/modules/A2/include
    ${CMAKE_SOURCE_DIR}/modules/M1/include
    ${CMAKE_SOURCE_DIR}/modules/M2/include
    ${CMAKE_SOURCE_DIR}/common/math/include
    ${CMAKE_SOURCE_DIR}/common/kalman/include
)

target_link_libraries(test PUBLIC M1 M2 A1 A2 math kalman ${OpenCV_LIBS})
