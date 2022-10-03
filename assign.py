from random import shuffle
from collections import deque
from extras import jenny_check


class Workday:
    def __init__(self, workplace):
        self.workplace = workplace
        self.before_lunch = {"FM" : []}
        self.after_lunch = {"EM" : []}

    def assign_workers(self, names, slots):

        names = [i.capitalize() for i in names]
        shuffle(names)
        FM = dict(zip(slots, names))

        FM = jenny_check(FM, self.workplace)

        dequed_names = deque(names)
        dequed_names.rotate(1)

        EM = dict(zip(slots, list(dequed_names)))

        EM = jenny_check(EM, self.workplace)

        self.before_lunch["FM"].append(FM)
        self.after_lunch["EM"].append(EM)
