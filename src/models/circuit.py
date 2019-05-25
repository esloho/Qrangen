import qiskit


class Circuit:

    def __init__(self, n=1):
        self.qr = qiskit.QuantumRegister(n)
        self.cr = qiskit.ClassicalRegister(n)
        self.U = qiskit.QuantumCircuit(self.qr, self.cr)
        self.U.h(self.qr)
        self.U.measure(self.qr, self.cr)

    def to_qiskit(self):
        return self.U
