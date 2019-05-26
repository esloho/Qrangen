import json
from qiskit import IBMQ, Aer, execute
from qiskit.providers.ibmq import least_busy


class IBMDevice:

    def __init__(self, nqubits):
        load_credentials()
        self.backend = least_busy(IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and not x.configuration().simulator and not x.name() == 'ibmq_16_melbourne'))
        print(self.backend)

    def execute(self, circuit, shots=1):
        return qiskit_execution(circuit, self.backend, shots=shots)


class SimulationDevice:

    def __init__(self, nqubits):
        load_credentials()
        self.backend = IBMQ.backends()[-1]

    def execute(self, circuit, shots=1):
        return qiskit_execution(circuit, self.backend, shots=shots)


class LocalDevice:

    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def execute(self, circuit, shots=1):
        return qiskit_execution(circuit, self.backend, shots=shots)


def qiskit_execution(circuits, backend, shots):
    # q_circuits = list(map(lambda x: x.to_qiskit(), circuits))
    q_circuits = circuits.to_qiskit()
    return execute(q_circuits, backend, shots=shots, memory=True)


def load_credentials():
    try:
        with open('key.json', 'r+') as token_file:
            ibm_token_json = json.load(token_file)
        ibm_token = ibm_token_json['api_token']
        IBMQ.enable_account(ibm_token)
    except Exception as e:
        print('IBMQ Account could not be enabled!')
