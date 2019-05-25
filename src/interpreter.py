class Interpreter:

    def __init__(self):
        pass

    def extract_random_number(self, result):
        complete_string = ''.join(result.get_memory())
        return binary_to_decimal(complete_string)

def binary_to_decimal(b):
    return int(b,2)
