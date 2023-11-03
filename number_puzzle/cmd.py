from math import prod


def main():
    ns = sorted(list(range(10)), reverse=True)
    for ps in partition(ns):
        nums = list(map(lambda ds: int("".join(map(str, ds))), ps))
        pr = prod(nums)
        print(pr, ps, nums)


def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n+1:]
        # put `first` in its own subset
        yield [[first]] + smaller

