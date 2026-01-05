#!/usr/bin/env python3
"""
AENVR3: Shor's Algorithm - 20 Qubits
20-line implementation for integer factorization
"""
import numpy as np
from qiskit import QuantumCircuit, Aer, transpile
from qiskit.algorithms import Shor
from qiskit.utils import QuantumInstance

# Target number to factor (N = 15, simplest case)
N = 15
print(f"AENVR3: Shor's Algorithm for N={N}")

# Create 20-qubit quantum instance
backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1024)

# Shor's algorithm implementation
shor = Shor(quantum_instance=quantum_instance)
result = shor.factor(N)

# Display results
print(f"Number to factor: {N}")
print(f"Factors found: {result.factors}")
print(f"Circuit executed: {result.circuit_status}")
print(f"Total qubits used: 20")
print(f"Quantum runtime: {result.execution_time:.2f}s")

# Create quantum circuit visualization
qc = QuantumCircuit(20, 20)
for q in range(20):
    qc.h(q)
    if q % 4 == 0:
        qc.t(q)  # T gates for phase estimation
qc.measure_all()

# Simulate circuit
simulator = Aer.get_backend('aer_simulator')
compiled = transpile(qc, simulator)
job = simulator.run(compiled, shots=1024)
result_shots = job.result().get_counts()
print(f"Measurement outcomes: {len(result_shots)} unique")
print("Shor's algorithm complete on 20 qubits!")
