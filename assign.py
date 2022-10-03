from random import shuffle
from collections import deque
from extras import jenny_check


class Workday:
    def __init__(self, workplace):
        self.workplace = workplace
        self.before_lunch = []
        self.after_lunch = []

    def __repr__(self):
        new_line = "\n"
        return f"Workplace: {self.workplace}{new_line}Before lunch: {self.before_lunch[0]}{new_line}After lunch: {self.after_lunch[0]}{new_line}"

    def assign_workers(self, names, slots):

        names = [i.capitalize() for i in names]
        shuffle(names)
        FM = dict(zip(slots, names))

        FM = jenny_check(FM)

        dequed_names = deque(names)
        dequed_names.rotate(1)

        EM = dict(zip(slots, list(dequed_names)))

        EM = jenny_check(EM)

        self.before_lunch.append(FM)
        self.after_lunch.append(EM)
