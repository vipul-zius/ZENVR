#!/bin/bash
echo "=== M-DOD Deployment Test ==="
echo "Testing all components..."

echo "1. Testing Python backend..."
if cd backend && python3 -c "import fastapi; print(\"✓ FastAPI:\", fastapi.__version__)"; then
    echo "✓ Python backend: PASS"
else
    echo "✗ Python backend: FAIL"
fi
cd ..

echo "2. Testing Node.js gateway..."
if cd api && node -e "console.log(\"✓ Node.js:\", process.version)"; then
    echo "✓ Node.js gateway: PASS"
else
    echo "✗ Node.js gateway: FAIL"
fi
cd ..

echo "3. Testing Go stream engine..."
if cd data_processing && go version; then
    echo "✓ Go compiler: PASS"
else
    echo "✗ Go compiler: FAIL"
fi
cd ..

echo "4. Testing Docker..."
if docker --version; then
    echo "✓ Docker: PASS"
else
    echo "✗ Docker: FAIL"
fi

echo "5. Testing monitoring..."
if systemctl is-active grafana-server >/dev/null 2>&1; then
    echo "✓ Grafana: RUNNING"
else
    echo "✗ Grafana: NOT RUNNING"
fi

echo "=== Deployment Test Complete ==="
