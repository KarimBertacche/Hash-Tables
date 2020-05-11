# initialize cache using a dictionary
cache = {}

def expensive_seq(x, y, z):
    # Implement me

    # check if key is present in cache
    if f"({x}, {y}, {z})" in cache.keys():
        # if so return by avoiding complex and expensive computations
        return cache[f"({x}, {y}, {z})"]
    
    # initialize a result variable
    result = None

    # if x is 0 or negative number
    if x <= 0:
        # store the sum of y + z in result
        result = y + z
    else:
        # else, make the expensive calculation and store it in results
        result = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
    
    # cache result for next time retrieval
    cache[f"({x}, {y}, {z})"] = result
    # return result
    return result

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
