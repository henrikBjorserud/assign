from collections import deque


def jenny_check(shift):
    """Check value of JK or MJ and rotate accordingly"""

    if (len(shift)) == 3:
        que_number = 2
    else:
        que_number = 1

    if (
        "JK" in shift
        and shift.get("JK") == "Jenny"
        or "MW, TA, SF" in shift
        and shift.get("MW, TA, SF") == "Jenny"
        or "MW, TA" in shift
        and shift.get("MW, TA") == "Jenny"
    ):
        dequed_values = deque(shift.values())
        dequed_values.rotate(que_number)
        return dict(zip(shift.keys(), dequed_values))
    else:
        return shift
