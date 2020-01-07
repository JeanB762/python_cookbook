# If you want to create a dictionary, and you also want to control the
# order of items when iterating or serializing.

from collections import OrderedDict

d = OrderedDict()

d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

print('#############################################################################################')
# if you want to precisely control the order of fields
# appearing in a JSON encoding, first building the
# data in an OrderedDict will do the trick:

import json

djson = json.dumps(d)

print(djson)