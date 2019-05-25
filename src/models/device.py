from qiskit import IBMQ, Aer, execute
from qiskit.providers.ibmq import least_busy


class IBMDevice:

    def __init__(self, nqubits):
        IBMQ.load_accounts()
        self.backend = least_busy(IBMQ.backends(filters=lambda x: x.configuration().n_qubits >= nqubits and not x.configuration().simulator))

    def execute(self, circuit):
        self.backend.execute(circuit)


class LocalDevice:

    def __init__(self, shots):
        self.backend = Aer.get_backend('qasm_simulator')
        self.shots = shots

    def execute(self, circuit):
        job = execute(circuit, self.backend, self.shots)
        result = job.result()

        return result
