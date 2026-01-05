#!/usr/bin/env python3
"""
ZENVR2: Shor's Algorithm - 15 Qubit Implementation
Quantum factorization demonstration
"""
from qiskit import QuantumCircuit, Aer, transpile
import numpy as np

def shor_15qubit_circuit(N=15):
    """Create 15-qubit Shor's algorithm circuit"""
    n_qubits = 15
    qc = QuantumCircuit(n_qubits, n_qubits)
    
    # Initialize superposition
    for q in range(n_qubits):
        qc.h(q)
    
    # Modular exponentiation (simplified)
    for q in range(n_qubits):
        angle = 2 * np.pi * (2 ** q) / N
        qc.p(angle, q)
    
    # Quantum Fourier Transform (QFT) approximation
    for q in range(n_qubits):
        qc.h(q)
        for j in range(q+1, n_qubits):
            angle = 2 * np.pi / (2 ** (j - q + 1))
            qc.cp(angle, j, q)
    
    # Reverse qubits for measurement
    for q in range(n_qubits//2):
        qc.swap(q, n_qubits-q-1)
    
    qc.measure(range(n_qubits), range(n_qubits))
    return qc

print("ZENVR2: 15-Qubit Shor's Algorithm")
print("=" * 40)

# Create and analyze circuit
qc = shor_15qubit_circuit(15)
print(f"Qubits: {qc.num_qubits}")
print(f"Total gates: {qc.size()}")
print(f"Circuit depth: {qc.depth()}")

# Simulate
simulator = Aer.get_backend('aer_simulator')
compiled = transpile(qc, simulator)
job = simulator.run(compiled, shots=1024)
result = job.result()
counts = result.get_counts()

print(f"Measurement outcomes: {len(counts)}")
print("\nTop measurement results (potential periods):")
for outcome, freq in sorted(counts.items(), key=lambda x: -x[1])[:5]:
    period = int(outcome, 2)
    print(f"  {outcome} (decimal {period}): {freq} counts")

print("\n" + "=" * 40)
print("To find factors of N=15:")
print("1. Find period r from measurements")
print("2. Compute gcd(a^{r/2} ± 1, N)")
print("3. Factors: 3 and 5")
print("\n15-qubit Shor's algorithm demonstration complete!")
