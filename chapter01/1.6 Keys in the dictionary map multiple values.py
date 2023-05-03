d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

from collections import defaultdict

def case01():
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print(d)

# case01()

def case02():
    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['d'].add(4)
    print(d)

# case02()

def case03():
    d = {}
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)
    print(d)

# case03()


def case04():
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)

# case04()