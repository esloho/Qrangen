import datetime
import numpy as np

from src.generator import Generator
from utils.graphics import visualize_demo
from utils.math import nth_moment, mean_of_square_RN


class Benchmark:

    def __init__(self, mode=0, iterations=1, bits=1):
        self.mode = mode
        self.iterations = iterations
        self.bits = bits
        self.upper_bound = 2**bits
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%dT%H%M%S')
        self.data_dir = './data/'

    def execute(self):
        results = {'Qrangen': [], 'np': []}
        all_data = {
            'Qrangen': self.generate_qrangen_data(),
            'np': self.generate_np_data()
        }

        bunches = [int(self.iterations*i/30) for i in range(1,30)]

        for key in all_data:
            for bunch in bunches:
                # mean = nth_moment(all_data[key][:bunch], 1)
                mean = mean_of_square_RN(all_data[key][:bunch], self.upper_bound)
                results[key].append(mean)

        self.save_data_to_disk(results, 'benchmark')

        visualize_demo(results, bunches)
        return results

    def generate_qrangen_data(self):
        qrangen = Generator(self.mode, self.iterations, self.bits)
        data = qrangen.generate_number()
        self.save_data_to_disk(data, 'Qrangen')

        return data

    def generate_np_data(self):
        np_random_list = list()
        for i in range(self.iterations):
            np_random_list.append(np.random.randint(low=0, high=self.upper_bound))

        self.save_data_to_disk(np_random_list, 'np')
        return np_random_list

    def save_data_to_disk(self, data, filename):
        filepath = self.data_dir + filename + '_' + self.timestamp + '.txt'
        content = str(data)

        with open(filepath, 'x') as f:
            f.write(content)
