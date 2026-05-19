find_package(OpenCV REQUIRED)

set(kalman_INCLUDE_DIR ${CMAKE_CURRENT_LIST_DIR}/include)

add_library(kalman INTERFACE)

target_include_directories(kalman INTERFACE 
    ${kalman_INCLUDE_DIR}
    ${OpenCV_INCLUDE_DIRS}
)

target_link_libraries(kalman INTERFACE ${OpenCV_LIBS})

set(kalman_INCLUDE_DIRS ${kalman_INCLUDE_DIR} ${OpenCV_INCLUDE_DIRS}
                        CACHE PATH "kalman filter include directories")
