class Interpreter:

    def __init__(self, mode='binary'):
        self.mode = mode

    def extract_random_number(self, result):

        if self.mode == 'binary':
            return result.get_memory()
        else:
            return [int(i, 2) for i in result.get_memory()]

        #interpreted_result = list()
        #for sub_result in result.get_memory():
        #    interpreted_result.append(binary_to_decimal(sub_result))
        #return interpreted_result

def binary_to_decimal(b):
    return int(b,2)
