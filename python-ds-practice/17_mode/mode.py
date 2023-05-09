def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counts = {}
    max_count = 0
    mode = None

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > max_count:
            max_count = counts[num]
            mode = num

    return mode