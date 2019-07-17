#include "whereami.h"
#include <iostream>

int main() {
  int length = wai_getExecutablePath(NULL, 0, NULL);

  char *path = new char[length + 1];
  wai_getExecutablePath(path, length, NULL);
  path[length] = '\0';

  std::cout << "Executable path: " << path << "\n";

  delete[] path;
  return 0;
}
