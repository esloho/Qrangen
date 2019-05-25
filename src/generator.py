from src.interpreter import Interpreter
from src.executor import Executor
from src.models.circuit import Circuit


class Generator:

    def __init__(self):
        pass

    def generate_number(self):
        circuit = self.__build_circuit__()
        execution = self.__run_circuit__(circuit)
        number = self.__get_random_number__(execution)
        return number

    def __build_circuit__(self):
        # TODO: Init circuit with params blablabla
        circuit = Circuit()
        return circuit

    def __run_circuit__(self, circuit):
        executor = Executor()
        return executor.simulate(circuit)

    def __get_random_number__(self, execution):
        interpret = Interpreter()
        number = interpret.extract_random_number(execution)
        return number
