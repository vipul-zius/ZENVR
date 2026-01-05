#!/bin/bash
echo "🚀 AENVR2 Quantum 23-Qubit Demo"
echo "================================"
python3 quantum_23qubits.py
echo ""
echo "📊 To create animated GIF (requires ImageMagick):"
echo "convert -delay 100 -loop 0 quantum*.png quantum_animation.gif"
echo ""
echo "✅ Demo complete!"
