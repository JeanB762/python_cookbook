# Unpacking of tagged tuples of varying sizes
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print (name)
print(email)
print(phone_numbers)

phone1, phone2 = phone_numbers
print(phone1)
print(phone2)


numbers = [1, 2, 3, 10, 8, 52, 15]
first, *middle, last = numbers

print(first)
print(middle)
print(last)

##############################################


records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:  #tag pick the first paramenter and *args pick anothers
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(args)


##Star unpacking can also be used with kinds of string processing such as splitting.
#Example

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)


###################################################################################
items = [1, 10, 7, 4, 5, 9]
head, *tail = items

print(head)
print(tail)


def sum(items):         #the kind of recursive sum with splitting
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))