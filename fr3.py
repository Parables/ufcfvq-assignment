from utils import data


def min_max_count(iterable):
    it = iter(iterable)
    min = next(it)
    max = min

    for x in it:
        if(x < min):
            min = x
        elif x > max:
            max = x
    return {
        'min': min,
        'min-count': iterable.count(min),
        'max': max,
        'max-count': iterable.count(max),
    }
