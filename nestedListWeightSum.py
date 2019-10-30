# recursive method that sums a nested list, where values in the list are
# counted as value * depth.


def depthSum(l, depth=-1):
    if depth == -1:
        return depthSum(l, 1)
    else:
        sum = 0
        for n in l:
            if isinstance(n, int):
                sum += n * depth
            else:
                sum += depthSum(n, depth + 1)
    return sum


def main():
    l = [[1, 1], 2, [1, 1]]
    print(depthSum(l))


if __name__ == "__main__":
    main()
