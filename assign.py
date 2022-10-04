from random import shuffle
from support import rotate_names, jenny_check


class Workday:
    """Assign worker names to shifts before lunch and after lunch without repeating the composition"""

    def __init__(self, workplace):
        self.workplace = workplace
        self.before_lunch = []
        self.after_lunch = []

    def __repr__(self):
        """Details of how the class is represented"""
        new_line = "\n"
        return f"Workplace: {self.workplace}{new_line}Before lunch: {self.before_lunch[0]}{new_line}After lunch: {self.after_lunch[0]}{new_line}"

    def assign_workers(self, names, slots):

        shuffle(names)  # initial shuffle to assure randomness
        FM = dict(zip(slots, names))  # make dictionary of slots and names
        if jenny_check(FM):  #  check if jenny is assigned to wrong shift
            FM = rotate_names(FM)

        EM = rotate_names(FM)  # rotate to ensure FM != EM
        while jenny_check(EM) or EM == FM:  # check jenny agin for EM
            EM = rotate_names(EM)

        self.before_lunch.append(FM)
        self.after_lunch.append(EM)
