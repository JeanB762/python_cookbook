# The heapq module has two functions— nlargest() and nsmallest() —that do exactly what you want.
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3, nums))
print("####################################")

#Both functions also accept a key parameter that allows them to be 
# used with more complicated data structures.

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name':  'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print('cheap: ',cheap)
print('expensive: ', expensive)

print('##################################################################################')


nums = ['sardinha', 'melao','machimbombo', 'abacate', 'chantili', 'cacatua', 'morango']
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)

#The most important feature of a heap is that heap[0] is always the smallest item. More‐
# over, subsequent items can be easily found using the heapq.heappop() method, which
# pops off the first item and replaces it with the next smallest item

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heap)