import json
from qiskit import IBMQ, Aer, execute
from qiskit.providers.ibmq import least_busy


class IBMDevice:

    def __init__(self, nqubits):
        IBMQ.load_accounts()
        self.backend = least_busy(IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and not x.configuration().simulator))

    def execute(self, circuit, shots=1024):
        return qiskit_execution(circuit, self.backend, shots)


class SimulationDevice:

    def __init__(self, nqubits):
        self.backend = least_busy(IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and x.configuration().simulator))

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

def load_credentials():
    try:
        with open('key.json', 'r+') as token_file:
            ibm_token = json.loads(token_file)
        IBMQ.enable_account(ibm_token)
    except Exception as e:
        print('IBMQ Account could not be enabled!')
