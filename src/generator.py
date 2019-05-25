from src.interpreter import Interpreter
from src.executor import Executor
from src.models.circuit import Circuit


class Generator:

    def __init__(self, mode=0, amount=1, bits=1):
        self.mode = mode
        self.amount = amount
        self.bits = bits

    def generate_number(self):
        circuit = self.__build_circuit__()
        result = self.__run_circuit__(circuit)
        number = self.__get_random_number__(result)

        return number

    def __build_circuit__(self):
        circuit = Circuit(self.bits)
        return circuit

    def __run_circuit__(self, circuit):
        executor = Executor(self.amount)
        if self.mode == 2:
            return executor.run(circuit, self.bits)
        if self.mode == 1:
            return executor.simulate(circuit, self.bits)
        return executor.local(circuit)

    def __get_random_number__(self, result):
        interpret = Interpreter(self.amount)
        number = interpret.extract_random_number(result)
        return number
