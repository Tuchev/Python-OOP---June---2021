def all_pemutations(seq):
    if len(seq) == 0:
        return []

    if len(seq) == 1:
        return [seq]

    l = []

    for i in range(len(seq)):
        m = seq[i]

        remlist = seq[:i] + seq[i+1:]

        for p in all_pemutations(remlist):
            l.append([m] + p)
    return l


def possible_permutations(seq):
    perms = all_pemutations(seq)
    for perm in perms:
        yield perm


[print(n) for n in possible_permutations([1, 2, 3])]