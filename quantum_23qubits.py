#!/usr/bin/env python3
"""
AENVR2: 23-Qubit Quantum Circuit Simulation
25-line quantum computing demonstration
"""
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create 23-qubit quantum circuit
qc = QuantumCircuit(23, 23)

# Add quantum gates
for qubit in range(23):
    qc.h(qubit)  # Hadamard gates
    if qubit % 3 == 0:
        qc.x(qubit)  # X gates on every 3rd qubit
    if qubit < 22:
        qc.cx(qubit, qubit+1)  # Entangle adjacent qubits

# Add measurement
qc.measure(range(23), range(23))

# Simulate
simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled, shots=1024).result()
counts = result.get_counts()

# Display results
print("AENVR2: 23-Qubit Quantum Circuit Results")
print("=" * 40)
print(f"Total qubits: 23")
print(f"Total gates: {qc.size()}")
print(f"Circuit depth: {qc.depth()}")
print(f"Measurement shots: 1024")
print(f"Unique outcomes: {len(counts)}")
print("\nTop 5 measurement outcomes:")
for outcome, count in sorted(counts.items(), key=lambda x: -x[1])[:5]:
    print(f"  {outcome}: {count} times ({count/10.24:.1f}%)")

# Create visualization
fig = plot_histogram(counts, title="AENVR2: 23-Qubit Results")
plt.savefig('quantum_results.png', dpi=100, bbox_inches='tight')
print("\nVisualization saved: quantum_results.png")
print("Run: display quantum_results.png or open the file")
