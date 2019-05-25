from qiskit import IBMQ

class IBMDevice:
    def __init__(self, nqubits):
        IBMQ.load_accounts()
        self.backend = least_busy(IBMQ.backends(filters = lambda x: x.configuration().n_qubits >= nqubits and not x.configuration().simulator))
    def execute(self, circuit):
        self.backend.execute(circuit)



class LocalDevice:
    pass
