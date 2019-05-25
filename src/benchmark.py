import datetime
import numpy as np
from src.generator import Generator

from utils.math import mean_of_square_RN


class Benchmark:

    def __init__(self, mode=0, iterations=1, bits=1):
        self.mode = mode
        self.iterations = iterations
        self.bits = bits
        self.upper_bound = 2**bits
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H%M%S')
        self.data_dir = './data/'

    def execute(self):
        results = {}
        all_data = {
            'Qrangen': self.generate_qrangen_data(),
            'np': self.generate_np_data()
        }

        for key in all_data:
            print(all_data[key])
            mean = mean_of_square_RN(all_data[key], self.upper_bound)
            results[key] = mean

        self.save_data_to_disk(results, 'benchmark')
        return results

    def generate_qrangen_data(self):
        qrangen = Generator(self.mode, self.iterations, self.bits)
        data = qrangen.generate_number()
        self.save_data_to_disk(data, 'Qrangen')

        return qrangen.generate_number()

    def generate_np_data(self):
        np_random_list = list()

        for i in range(self.iterations):
            np_random_list.append(np.random.randint(low=0, high=self.upper_bound))

        self.save_data_to_disk(np_random_list, 'np')

        return np_random_list

    def save_data_to_disk(self, data, filename):
        filepath = self.data_dir + filename + '_' + self.timestamp + '.txt'
        content = str(data)

        f = open(filepath, 'x')
        f.write(content)
