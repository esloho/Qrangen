from matplotlib import pyplot as plt

from src.generator import Generator

def run_plot(a):
    fig = plt.figure()
    fig.suptitle('run plot')
    plt.plot(
    [i for i in range(len(a))],
    a,
    marker = '.',
    linestyle = 'None')

def lag_plot(a):
    fig = plt.figure()
    fig.suptitle('lag plot')
    plt.plot(
    a[:-1],
    a[1:],
    marker = '.',
    linestyle = 'None')

def histogram(a,nbins):
    fig = plt.figure()
    plt.hist(a, nbins)

def correlogram(a):
    pass

def mean(a):
    pass

if __name__ == "__main__":
    mode = 0
    amount = 100
    bits = 5

    a = Generator(mode,amount,bits).generate_number()

    run_plot(a)
    lag_plot(a)
    histogram(a, 2**bits)
    correlogram(a)
    mean(a)

    plt.show()
