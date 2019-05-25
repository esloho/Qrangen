from src.models.device import IBMDevice, LocalDevice


class Executor:

    def __init__(self):
        pass

    def simulate(self, circuit):
        device = LocalDevice()
        return self.__execute__(device, circuit)

    def run(self, circuit):
        device = IBMDevice()
        return self.__execute__(device, circuit)

    def __execute__(self, device, circuit):
        job = device.execute(circuit)
        result = job.result()

        if not result.success:
            raise Exception('Execution of circuit failed')

        return result

