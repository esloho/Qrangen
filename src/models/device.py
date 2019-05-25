from qiskit import IBMQ, Aer, execute
from qiskit.providers.ibmq import least_busy


class IBMDevice:

    def __init__(self, nqubits):
        IBMQ.load_accounts()
        self.backend = least_busy(IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and not x.configuration().simulator))

    def execute(self, circuit, shots=1024):
        return qiskit_execution(circuit, self.backend, shots)


class LocalDevice:

    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def execute(self, circuit, shots=1024):
        return qiskit_execution(circuit, self.backend, shots)


def qiskit_execution(circuit, backend, shots):
    q_circuit = circuit.to_qiskit()
    return execute(q_circuit, backend, shots=shots)
