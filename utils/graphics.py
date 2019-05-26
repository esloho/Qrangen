from matplotlib import pyplot as plt
from utils.math import autocovariance, mean


def visualize(data, upper_bound):
    run_plot(data)
    lag_plot(data)
    histogram(data, upper_bound)
    correlogram(data)

    plt.show()


def visualize_demo(data, bunches):
    fig = plt.figure()
    fig.suptitle("2nd-order moments for normalized numpy's rand and Qrangen")
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.plot(bunches, data['np'])
    ax1.set_ylabel('numpy')
    ax1.set_xlabel('size of sample')
    ax2.plot(bunches, data['Qrangen'])
    ax2.set_ylabel('Qrangen')
    ax2.set_xlabel('size of sample')
    plt.show()


def run_plot(data):
    fig = plt.figure()
    fig.suptitle('run plot')
    plt.plot(
        [i for i in range(len(data))],
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

