def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    #  UPER : Need a function to find 2 items with a sum weight = to the weight limit.  Must return a tuple of numbers (zero, one)
    # Your code here

    data = {}
    for i in range(len(weights)):
        # loop through
        data[weights[i]] = i
        #  set the weight to a key
    for i in range(len(weights)):
        # loop for the range
        limweight = limit-weights[i]
        # calc the dif
        if limweight in data:
            #  if weight limit is in the data,
            return (max(i, data[limweight]), min(i, data[limweight]))

    return None
