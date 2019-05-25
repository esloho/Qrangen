from src.interpreter import Interpreter
from src.executor import Executor
from src.models.circuit import Circuit


class Generator:

    def __init__(self, mode=0, exponent):
        self.mode = mode
        self.exponent

    def generate_number(self):
        circuit = self.__build_circuit__(exponent)
        result = self.__run_circuit__(circuit)
        number = self.__get_random_number__(result)
        return number

    def __build_circuit__(self, exponent):
        circuit = Circuit(exponent)
        return circuit

    def __run_circuit__(self, circuit):
        executor = Executor()

        if self.mode == 2:
            return executor.run(circuit)

        if self.mode == 1:
            return executor.simulate(circuit)

        return executor.local(circuit)

    def __get_random_number__(self, result):
        interpret = Interpreter()
        number = interpret.extract_random_number(result)
        return number
