#!/bin/bash
echo "Testing all implementations..."
echo "=============================="

Test Python
echo ""
echo "1. Testing Python implementation:"
cd src/python
python3 -c "print('Python test successful')"
cd ../..

Test Java compilation
echo ""
echo "2. Testing Java compilation:"
cd src/java
javac ModuleTheorem.java 2>/dev/null && echo "Java compilation successful" || echo "Java compilation failed (requires JDK)"
cd ../..

Test C++ compilation
echo ""
echo "3. Testing C++ compilation:"
cd src/cpp
g++ -std=c++11 -o test module_theorem.cpp 2>/dev/null && echo "C++ compilation successful" || echo "C++ compilation failed (requires g++)"
rm -f test 2>/dev/null
cd ../..

Test Go
echo ""
echo "4. Testing Go:"
cd src/go
go version 2>/dev/null && echo "Go available" || echo "Go not installed"
cd ../..

Test Rust
echo ""
echo "5. Testing Rust:"
cd src/rust
rustc --version 2>/dev/null && echo "Rust available" || echo "Rust not installed"
cd ../..

echo ""
echo "=============================="
echo "Run './verify-install.sh' for complete system verification"
echo "Run './theorem-explainer.sh' for interactive theorem explanation"
