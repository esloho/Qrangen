from src.models.backend import IBMBackend, LocalBackend


class Executor:

    def __init__(self):
        pass

    def simulate(self, method, circuit):
        backend = IBMBackend()

    def run(self, method, circuit):
        backend = LocalBackend()
