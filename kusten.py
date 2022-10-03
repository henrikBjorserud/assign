from random import shuffle
from time import sleep
from collections import deque
import json


def export(FM, EM):
    """Export results to txt-file"""
    whole_day = {"FM": FM, "EM": EM}
    with open("dagens.txt", "w") as out_file:
        json.dump(whole_day, out_file, indent=4, ensure_ascii=False)


def jenny_check(shift):
    """Check value of AJ and rotate accordingly"""

    if (len(shift)) == 4:
        que_number = -1
    else:
        que_number = 1

    if shift.get("AJ") == "Jenny":
        dequed_values = deque(shift.values())
        dequed_values.rotate(que_number)
        return dict(zip(shift.keys(), dequed_values))
    else:
        return shift


def assignment(names):
    """Assign workers to slots"""

    four_slots = ["AJ", "AH, SG", "RO, UA, AHA", "MW, TA, SF"]
    five_slots = ["AJ", "MW, TA", "RO, UA", "AH, SG", "AHA, SF"]

    if len(names) == 4:
        slots = four_slots

    else:
        slots = five_slots

    names = [i.capitalize() for i in names]
    shuffle(names)
    FM = dict(zip(slots, names))

    FM = jenny_check(FM)

    dequed_names = deque(names)
    dequed_names.rotate(1)

    EM = dict(zip(slots, list(dequed_names)))

    EM = jenny_check(EM)

    return FM, EM


def worker_names(num_names):
    """Ask for names of personel"""

    names = []
    for i in range(num_names):
        print("-" * 14)
        name = input("Skriv ett namn och tryck enter: ")
        names.append(name)
        print("-" * 14)
        print(f"Tillagda namn: {', ' .join(names)}")

    FM, EM = assignment(names)

    return FM, EM


def number_of_names():
    """Ask user for number of personel"""

    print("hur många personal vill du fördela?\n")

    num_names = input("ange 4 eller 5: ")

    if num_names == "4" or "5":
        fm, em = worker_names(int(num_names))

    else:
        print("försök igen")
        sleep(3)
        main()

    return fm, em


def main():
    """run functions when script runs and print the result"""

    fm, em = number_of_names()

    print("-" * 14)
    print("morgonen:")
    print(json.dumps(fm, indent=4))
    print("-" * 14)
    print("eftermiddagen:")
    print(json.dumps(em, indent=4))

    to_export = input("vill du skriva resultatet till en fil? (y/n)")

    if to_export == "y":
        export(fm, em)

    else:
        print("avslutar...")
        sleep(3)


if __name__ == "__main__":
    main()
