#unpacking sequences into separate varibles

p = (4,5)
x, y = p        #If there is a mismatch in the number of elements, you’ll get an error!!!
print(x)
print(y)

data = ['ACME', 50, 90.1, (2012, 12, 21)]
name, shares, price, date = data

print(name)
print(shares)
print(price)
print(date)

name, shares, price, (year, mon, day) = data

print(name)
print(shares)
print(price)
print(day, mon, year)


str1 = "hello"
a, b, c, d, e = str1

print(a)
print(b)
print(c)
print(d)
print(e)

#to discard some values, you can pick a throwaway varible name for it.
#Example

_, shares, price, _ = data      
print(shares)
print(price)

#However, make sure that the variable name you pick isn’t being used for something else already.


