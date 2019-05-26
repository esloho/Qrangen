from matplotlib import pyplot as plt
from utils.math import autocovariance, mean


def visualize(data, upper_bound):
    run_plot(data)
    lag_plot(data)
    histogram(data, upper_bound)
    correlogram(data)

    plt.show()


def run_plot(data):
    fig = plt.figure()
    fig.suptitle('run plot')
    plt.plot(
        range(len(data)),
        data,
        marker='.',
        linestyle='None')


def lag_plot(data):
    fig = plt.figure()
    fig.suptitle('lag plot')
    plt.plot(
        data[:-1],
        data[1:],
        marker='.',
        linestyle='None')


def histogram(data, bits):
    fig = plt.figure()
    plt.hist(data, bits)


def correlogram(data):
    fig = plt.figure()
    fig.suptitle('correlogram')
    ma = mean(data)
    hs = range(len(data))
    av = [autocovariance(data, h, ma) for h in hs]
    plt.plot(hs, av)

