"""Basic tests for quantum flight search application."""
import unittest
import sys
sys.path.append('src')

from quantum.flight_optimizer import QuantumFlightOptimizer

class TestQuantumOptimizer(unittest.TestCase):
    def test_qubit_initialization(self):
        optimizer = QuantumFlightOptimizer(qubits=24)
        self.assertEqual(optimizer.n_qubits, 24)
        
    def test_circuit_creation(self):
        optimizer = QuantumFlightOptimizer(qubits=24)
        oracle = optimizer.create_flight_oracle({})
        self.assertEqual(oracle.num_qubits, 24)

if __name__ == '__main__':
    unittest.main()
