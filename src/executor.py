from src.models.device import IBMDevice, LocalDevice, SimulationDevice


class Executor:

    def __init__(self, iterations=1):
        self.iterations = iterations

    def local(self, circuit):
        return self.__execute__(LocalDevice(), circuit)

    def simulate(self, circuit, nqubits):
        return self.__execute__(SimulationDevice(nqubits), circuit)

    def run(self, circuit, nqubits):
        return self.__execute__(IBMDevice(nqubits), circuit)

    def __execute__(self, device, circuit):
        job = device.execute(circuit, self.iterations)
        result = job.result()

        if not result.success:
            raise Exception('Execution of circuit failed')

        return result

