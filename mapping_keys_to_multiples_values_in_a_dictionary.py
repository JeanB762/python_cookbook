from collections import defaultdict

d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['a'].append(4)

d1 = defaultdict(set)

d1['a'].add(1)
d1['a'].add(2)
d1['a'].add(4)