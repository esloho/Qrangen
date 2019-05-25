class Interpreter:

    def __init__(self, n=1, mode='decimal'):
        self.mode = mode
        self.n = n

    def extract_random_number(self, result):
        numbers = [tuple(result.get_counts(i).keys())[0] for i in range(self.n)]
        if self.mode == 'binary':
            return numbers
        else:
            return [int(number, 2) for number in numbers]

def binary_to_decimal(b):
    return int(b,2)
