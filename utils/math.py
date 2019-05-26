def nth_moment(sample, n, centered=False, scaled=True, upper_bound=2):
    if not scaled:
        scaled_sample = [x / upper_bound for x in sample]
    else:
        scaled_sample = sample
    if centered:
        mean = nth_moment(scaled_sample, n, centered=False)
        centered_sample = [element - mean for element in scaled_sample]
        return (1/len(scaled_sample)) * sum([abs(element) ** n  for element in centered_sample])
    return (1/len(scaled_sample)) * sum([abs(element) ** n  for element in scaled_sample])


def mean(a):
    return nth_moment(a, 1)

def mean_of_square_RN(data, upper_bound):
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
