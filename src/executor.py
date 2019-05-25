from src.models.device import IBMDevice, LocalDevice


class Executor:

    def __init__(self):
        pass

    def simulate(self, method, circuit):
        backend = IBMDevice()
        backend.execute(circuit)

    def run(self, method, circuit):
        backend = LocalDevice()
