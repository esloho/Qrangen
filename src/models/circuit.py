import qiskit


class Circuit:

    def __init__(self):
        self.qr = qiskit.QuantumRegister(1)
        self.cr = qiskit.ClassicalRegister(1)
        self.U = qiskit.QuantumCircuit(self.qr, self.cr)
        self.U.h(self.qr)

    def to_qiskit(self):
        return self.U
