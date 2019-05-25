from src.executor import Executor


class Generator:

    def __init__(self):
        pass

    def generate_number(self):
        pass

    def __run_circuit__(self, circuit):
        executor = Executor()
        executor.simulate('method', circuit)
