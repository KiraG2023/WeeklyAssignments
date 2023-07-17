def summation (lower, upper):
    """ Returns the sum of the number from lower through upper."""
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: x + y,
                      range(lower, upper + 1))
print("the average is:", average)
