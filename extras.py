from collections import deque


def jenny_check(shift, person):
    """Check value of JK or MJ and rotate accordingly"""

    if (len(shift)) == 3 or 5:
        que_number = -1
    else:
        que_number = 1

    if shift.get(person) == "Jenny":
        dequed_values = deque(shift.values())
        dequed_values.rotate(que_number)
        return dict(zip(shift.keys(), dequed_values))
    else:
        return shift
