from collections import defaultdict, OrderedDict


def groupby(func, seq):
    """Apply  `func` to `seq` elements and group by result"""
    result = defaultdict(list)

    for element in seq:
        result[func(element)].append(element)

    return result


def compose(func1, func2):
    return lambda arg: func1(func2(arg))


def iterate(func):
    """Create function generator that iterates `func`."""
    iterated_function = lambda arg: arg

    while True:
        yield iterated_function
        iterated_function = compose(func, iterated_function)


def zip_with(func, *iterables):
    """Create a function generator that returns a sequence of elements,
    where each element is the result of `func` applied to the corresponding
    elemens of all `iterables`.

    """
    for args in zip(*iterables):
        yield func(*args)


def cache(func, cache_size):
    """Keep in cache the last `cache_size` unique calls of a `func`."""
    cache_storage = OrderedDict()

    def check_and_modify_cache(*args):
        if args in cache_storage:
            return cache_storage[args]
        else:
            result = cache_storage[args] = func(*args)
            if len(cache_storage) > cache_size:
                cache_storage.popitem(last=False)
            return result

    return check_and_modify_cache
