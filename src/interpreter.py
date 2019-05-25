class Interpreter:

    def __init__(self, mode='binary'):
        self.mode = mode

    def extract_random_number(self, result):
        if self.mode == 'binary':
            return result.get_memory()
        else:
            return [int(i,2) for i in result.get_memory()]
