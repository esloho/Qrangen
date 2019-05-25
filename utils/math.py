def nth_moment(sample, n, centered=False):

    if centered:
        mean = nth_moment(sample,n, centered=False)
        centered_sample = [element - mean for element in sample]
        return (1/len(sample)) * sum([abs(element ** n)  for element in centered_sample])

    return (1/len(sample)) * sum([element ** n  for element in sample])


def mean_of_square_RN( data, upper_bound):
    n = len(data)

    if max(data) > 1:
        normalized_data = [x / upper_bound for x in data]
        return (1/n) * sum([point**2 for point in normalized_data])

    return (1/n) * sum([point**2 for point in data])
