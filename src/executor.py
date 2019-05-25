from src.models.device import IBMDevice, LocalDevice, SimulationDevice


class Executor:

    def __init__(self):
        pass

    def local(self, circuit):
        return self.__execute__(LocalDevice(), circuit)

    def simulate(self, circuit):
        return self.__execute__(SimulationDevice(), circuit)

    def run(self, circuit):
        return self.__execute__(IBMDevice(), circuit)

    def __execute__(self, device, circuit):
        job = device.execute(circuit)
        result = job.result()

        if not result.success:
            raise Exception('Execution of circuit failed')

        return result

