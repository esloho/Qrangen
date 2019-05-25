from src.models.device import IBMDevice, LocalDevice


class Executor:

    def __init__(self):
        pass

    def simulate(self, circuit):
        device = LocalDevice(1024)
        result = device.execute(circuit)

        return result

    def run(self, method, circuit):
        device = IBMDevice()
        result = device.execute(circuit)

        return result

