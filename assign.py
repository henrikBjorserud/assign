from random import shuffle
from collections import deque
from extras import jenny_check


class Assign:
    def __init__(self, names, slots):
        self.names = names
        self.slots = slots

    def assign(self, names, slots):

        names = [i.capitalize() for i in names]
        shuffle(names)
        FM = dict(zip(slots, names))

        FM = jenny_check(FM)

        dequed_names = deque(names)
        dequed_names.rotate(1)

        EM = dict(zip(slots, list(dequed_names)))

        EM = jenny_check(EM)

        FM = {"FM": FM}

        EM = {"EM": EM}

        schedule = FM | EM

        return schedule
