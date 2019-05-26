def nth_moment(sample, n, centered=False):

    if centered:
        mean_value = nth_moment(sample,n, centered=False)
        centered_sample = [element - mean_value for element in sample]
        return (1/len(sample)) * sum([abs(element ** n) for element in centered_sample])

    return (1/len(sample)) * sum([element ** n for element in sample])


def mean(a):
    return nth_moment(a, 1)


def mean_of_square_RN( data, upper_bound):
    n = len(data)

    if max(data) > 1:
        normalized_data = [x / upper_bound for x in data]
        return (1/n) * sum([point**2 for point in normalized_data])

    return (1/n) * sum([point**2 for point in data])


def autocovariance(a, h, ma=None):
    if ma is None:
        ma = mean(a)

    v = 0

    for i, _ in enumerate(a[:-h]):
        v += (a[i] - ma)*(a[i+h] - ma)

    return 1/len(a)*v


def variance(a, ma=None):
    if ma is None:
        ma = mean(a)

    v = 0

    for i in a:
        v += (i - ma)**2

    return 1/len(a)*v
