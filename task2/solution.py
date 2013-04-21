from collections import defaultdict, OrderedDict


def groupby(func, seq):
    result = defaultdict(list)
    for element in seq:
        result[func(element)].append(element)
    return result


def iterate(func):
    def repeated(n, arg):
        for i in range(n):
            arg = func(arg)
        return arg
    repeat = 0
    while True:
        yield lambda arg: repeated(repeat, arg)
        repeat += 1


def zip_with(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)


def cache(func, cache_size):
    cache_storage = OrderedDict()

    def check_and_modify_cache(arg):
        if arg in cache_storage:
            return cache_storage[arg]
        else:
            result = cache_storage[arg] = func(arg)
            if len(cache_storage) > cache_size:
                cache_storage.popitem(last=False)
            return result

    return lambda arg: check_and_modify_cache(arg)
