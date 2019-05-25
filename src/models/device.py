from qiskit import IBMQ, Aer, execute
from qiskit.providers.ibmq import least_busy


class IBMDevice:

    def __init__(self, nqubits, shots=1024):
        IBMQ.load_accounts()
        self.backend = least_busy(IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and not x.configuration().simulator))
        self.shots = shots

    def execute(self, circuit):
        return qiskit_execution(circuit, self.backend, self.shots)


class LocalDevice:

    def __init__(self, shots=1024):
        self.backend = Aer.get_backend('qasm_simulator')
        self.shots = shots

    def execute(self, circuit):
        return qiskit_execution(circuit, self.backend, self.shots)


def qiskit_execution(circuit, backend, shots):
    q_circuit = circuit.to_qiskit()
    return execute(q_circuit, backend, shots=shots)
