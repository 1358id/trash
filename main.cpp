#include "greet.hpp"
#include <iostream>
#include <string>

int main() {
  std::string name;
  std::cin >> name;
  greet(name);
  return 0;
}