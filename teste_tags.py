dados = [
    ('teste1', 2, 3),
    ('teste2', 'teste3'),
    ('teste1', 4, 5),
]

def test1(s, t):
    print('teste1', s, t)

def test2(a):
    print('teste2', a)


for tag, *args in dados:
    if tag == 'teste1':
        test1(*args)
    elif tag == 'teste2':
        test2(*args)