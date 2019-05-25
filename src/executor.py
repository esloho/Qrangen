from src.models.device import IBMDevice, LocalDevice


class Executor:

    def __init__(self):
        pass

    def simulate(self, circuit):
        device = LocalDevice(1024)
        return self.__execute__(device, circuit)

    def run(self, method, circuit):
        device = IBMDevice()
        return self.__execute__(device, circuit)

    def __execute__(self, device, circuit):
        job = device.execute(circuit)
        result = job.result()
        # TODO: check if job went well

        return result

