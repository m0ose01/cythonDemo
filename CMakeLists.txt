cmake_minimum_required(VERSION 3.22)
project(${SKBUILD_PROJECT_NAME} LANGUAGES C)

find_package(
  Python
  COMPONENTS Interpreter Development.Module
  REQUIRED)

set(C_LIB_PATH "c_lib")
add_subdirectory("${C_LIB_PATH}")

set(addone_path "src/cythondemo/addone.pyx")
set(shopping_list_path "src/cythondemo/shopping_list.pyx")

add_custom_command(
  OUTPUT addone.c
  COMMAND Python::Interpreter -m cython
          "${CMAKE_CURRENT_SOURCE_DIR}/${addone_path}" --output-file addone.c
  DEPENDS ${addone_path}
  VERBATIM)

add_custom_command(
  OUTPUT shopping_list.c
  COMMAND Python::Interpreter -m cython
          "${CMAKE_CURRENT_SOURCE_DIR}/${shopping_list_path}" --output-file shopping_list.c
  DEPENDS ${shopping_list_path}
  VERBATIM)

python_add_library(addone MODULE addone.c WITH_SOABI)
python_add_library(shopping_list MODULE shopping_list.c WITH_SOABI)
target_link_libraries(shopping_list PUBLIC items)
set_property(TARGET items PROPERTY POSITION_INDEPENDENT_CODE ON)
target_include_directories(shopping_list PUBLIC "${C_LIB_PATH}")

install(TARGETS addone DESTINATION ${SKBUILD_PROJECT_NAME})
install(TARGETS shopping_list DESTINATION ${SKBUILD_PROJECT_NAME})
