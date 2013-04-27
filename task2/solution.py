from collections import defaultdict, OrderedDict


def groupby(func, seq):
    result = defaultdict(list)

    for element in seq:
        result[func(element)].append(element)

    return result


def compose(func1, func2):
    return lambda arg: func1(func2(arg))


def iterate(func):
    iterated_function = lambda arg: arg

    while True:
        yield iterated_function
        iterated_function = compose(func, iterated_function)


def zip_with(func, *iterables):
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
