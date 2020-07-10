#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    #  Need a function to reconstruct the truip route from given tickets. Need to look at the source and the destination to link them up in order.
    #  Need to run a check to see if the destination = source of a different ticket.

#     tickets = [
#     Ticket{ source: "PIT", destination: "ORD" },
#     Ticket{ source: "XNA", destination: "CID" },
#     Ticket{ source: "SFO", destination: "BHM" },
#     Ticket{ source: "FLG", destination: "XNA" },
#     Ticket{ source: "NONE", destination: "LAX" },
#     Ticket{ source: "LAX", destination: "SFO" },
#     Ticket{ source: "CID", destination: "SLC" },
#     Ticket{ source: "ORD", destination: "NONE" },
#     Ticket{ source: "SLC", destination: "PIT" },
#     Ticket{ source: "BHM", destination: "FLG" }
# ]
    route = [None] * length
    #  set the route

    data = dict()
    #  set the dictionary
    for ticket in tickets:
        # loop for the tickets
        data[ticket.source] = ticket.destination
        # can hash each ticket such that the starting location is the key and the destination is the value.
    next = data["NONE"]
    # "NONE " from the test file

    for i in range(0, length):
        # loop thru the data
        route[i] = next
        next = data[next]
    return route
