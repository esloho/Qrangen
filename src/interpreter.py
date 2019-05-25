class Interpreter:

    def __init__(self):
        pass

    def extract_random_number(self, result):
        return [binary2decimal(i) for i in result.get_memory()]


def binary2decimal(string):
    maxp = len(string)
    n = 0
    for i in range(maxp):
        n += int(string[i]) * 2 ** (maxp - i)
    return n
