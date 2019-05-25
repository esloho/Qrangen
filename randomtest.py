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
    fig = plt.figure()
    fig.suptitle('correlogram')
    ma = mean(a)
    hs = range(len(a))
    av = [autocovariance(a, h, ma) for h in hs]
    plt.plot(hs,av)

def mean(a):
    return 1/len(a)*sum(a)

def variance(a, ma = None):
    if ma is None:
        ma = mean(a)
    v = 0
    for i in a:
        v += (i - ma)**2
    return 1/len(a)*v

def autocovariance(a, h, ma = None):
    if ma is None:
        ma = mean(a)
    v = 0
    for i,_ in enumerate(a[:-h]):
        v += (a[i] - ma)*(a[i+h] - ma)
    return 1/len(a)*v

if __name__ == "__main__":
    mode = 2
    amount = 1024
    bits = 12

    a = Generator(mode,amount,bits).generate_number()

    run_plot(a)
    lag_plot(a)
    histogram(a, 2**bits)
    correlogram(a)

    plt.show()
