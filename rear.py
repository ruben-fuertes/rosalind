from sys import argv


def tolist(string):
    """Get the numbers into a list."""
    return [int(num) for num in string.split(" ")]


def tolists(string):
    """Parse the inputs to lists."""
    lists_str = string.strip().split('\n')
    return tolist(lists_str[0]), tolist(lists_str[1])


def compute_breakpoints(start, target):
    """Find the points where adjacent numbers do not match in the two lists."""
    result = []
    # Add the last and the first numbers to the start and the target
    start_ext = [0] + start + [len(start)+1]
    target = [0] + target + [len(start)+1]

    for i, value in enumerate(start):
        i2 = target.index(value)
        previous_value = target[i2-1]
        if i2+1 > len(target)-1:
            next_value = target[0]
        else:
            next_value = target[i2+1]
        if start_ext[i] not in [previous_value, next_value]:
            result.append("...")
        result.append(value)
        if start_ext[i+2] not in [previous_value, next_value]:
            result.append("...")
    result = [value for i, value in enumerate(result) if result[i-1]!= result[i] or i == 0]
    return  result.count("...")#, result


def compute_reversals(sequence):
    """Perform all the posible reversals of a sequence."""
    reversals = []
    rev_perm = lambda perm, i, j: perm[:i] + perm[i:j + 1][::-1] + perm[j + 1:]
    for i, _ in enumerate(sequence):
        for j in range(i+1, len(sequence)):
            reversals.append(rev_perm(sequence, i, j))
    return reversals


def min_reversals(start, target):
    """Compute the minimum number of reversals."""

    breakpoints = compute_breakpoints(start, target)
    num_rev = 0
    sequences = [(start, breakpoints, num_rev)]

    while breakpoints != 0:
        new_seq = []
        num_rev += 1
        for seq in sequences:
            reversals = compute_reversals(seq[0])
            for rever in reversals:
                bkps = compute_breakpoints(rever, target)
                if bkps > breakpoints:
                    continue
                new_seq.append((rever, bkps, num_rev))
        sequences = sequences + new_seq
        breakpoints = min({seq[1] for seq in sequences})
        sequences = [seq for seq in sequences if seq[1] == breakpoints]
    return min([seq[2] for seq in sequences]), sequences


if __name__ == "__main__":
    with open(argv[1]) as file:
        inputs = file.read()
    for pair in inputs.split("\n\n"):
        start, target = tolists(pair)
        min_revs = min_reversals(start,target)
        print(min_revs[0])
