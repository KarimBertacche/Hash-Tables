import math
import random

# add a cache to speed up performance
cache = {}

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster

    # if the string is present in the cache
    if f"{x}**{y}" in cache.keys():
        # return it to avoid complex calculations
        return cache[f"{x}**{y}"]
    # else go through the normal process
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    # cache result for next time is retrieved
    cache[f"{x}**{y}"] = v

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
