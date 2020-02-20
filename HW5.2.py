          # Will there be enough space?

def enough(cap, on, wait):
    if cap < on + wait:
        return on+wait-cap
    else:
        return 0
print(enough(10, 5, 5))