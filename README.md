# Use .so file code in Python
## 1. Make .so file
g++ -fPIC -c ./SimpleMC.cpp ./Random1.cpp
g++ -shared ./SimpleMC.o ./Random1.o -o libSimpleMC.so

## 2. Call C++ code in .py file
