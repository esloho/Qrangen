from qiskit import IBMQ, Aer, execute
from qiskit.providers.ibmq import least_busy


class IBMDevice:

    def __init__(self, nqubits):
        load_credentials()
        self.backend = least_busy(IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and not x.configuration().simulator))

    def execute(self, circuit, shots=1):
        return qiskit_execution(circuit, self.backend, shots)


class SimulationDevice:

    def __init__(self, nqubits):
        load_credentials()
        # self.backend = IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and x.configuration().simulator)[0]
        self.backend = IBMQ.backends()[-1]

    def execute(self, circuit, shots=1):
        return qiskit_execution(circuit, self.backend, shots)


class LocalDevice:

    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def execute(self, circuit, shots=1):
        return qiskit_execution(circuit, self.backend, shots)


def qiskit_execution(circuit, backend, shots):
    q_circuit = circuit.to_qiskit()
    return execute(q_circuit, backend, shots=shots, memory=True)


def load_credentials():
    try:
        with open('token', 'r') as token_file:
            token = token_file.read()
        IBMQ.enable_account(token)
    except Exception as e:
        print('IBMQ Account could not be enabled!')
