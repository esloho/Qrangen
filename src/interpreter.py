class Interpreter:

    def __init__(self, n=1, mode='decimal'):
        self.mode = mode
        self.n = n

    def extract_random_number(self, result):
        numbers = result.get_memory()
        if self.mode == 'binary':
            return numbers
        else:
            return [int(number, 2) for number in numbers]

def binary_to_decimal(b):
    return int(b,2)
