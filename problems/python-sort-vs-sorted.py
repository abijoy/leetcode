import time, random

lst = [random.randint(0, 10000000) for _ in range(10000000)]

# Measure the time taken to sort the list using sort()
start_time = time.time()
lst.sort()
print("sort() took %.6f seconds" % (time.time() - start_time))

# Measure the time taken to sort the list using sorted()
start_time = time.time()
sorted_lst = sorted(lst)
print("sorted() took %.6f seconds" % (time.time() - start_time))


# End of story: though both sort() and sorted() both have
# complexity of O(nlogn), sort() do sorting by modifying the original list
# and sorted() creates a new list(space: O(n)) which is sorted keeping the original list untouched
# sorted() is way faster than sort()
# so it's better use sorted() if using extra O(n) space. 
