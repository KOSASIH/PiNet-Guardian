import numpy as np
from qiskit import QuantumCircuit, execute

class QuantumKeyDistribution:
    def __init__(self):
        self.qc = QuantumCircuit(2)

    def generate_key(self):
        self.qc.h(0)
        self.qc.cx(0, 1)
        self.qc.measure_all()
        job = execute(self.qc, backend="qasm_simulator")
        result = job.result()
        key = result.get_counts()
        return key

    def encode_message(self, message, key):
        encoded_message = ""
        for i, bit in enumerate(message):
            if key[i] == "0":
                encoded_message += str(bit)
            else:
                encoded_message += str(1 - bit)
        return encoded_message

    def decode_message(self, encoded_message, key):
        decoded_message = ""
        for i, bit in enumerate(encoded_message):
            if key[i] == "0":
                decoded_message += str(bit)
            else:
                decoded_message += str(1 - bit)
        return decoded_message
