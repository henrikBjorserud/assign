import json
from collections import deque

"""Assisting functions"""


def names(num_names):
    """Ask for names of personel"""

    worker_names = []
    for i in range(num_names):
        print("-" * 14)
        name = input("Skriv ett namn och tryck enter: ")
        worker_names.append(name)
        print("-" * 14)
        print(f"Tillagda namn: {', ' .join(worker_names)}")

    worker_names = [i.capitalize() for i in worker_names]
    worker_names = [i.strip() for i in worker_names]

    return worker_names


def export(schedule):
    """Export results to txt-file"""
    with open("dagens.txt", "w") as out_file:
        json.dump(schedule.__dict__, out_file, indent=4, ensure_ascii=False)

    return "Schedule Exported"


def rotate_names(shift):
    """Use deque to rotate names"""
    dequed_values = deque(shift.values())
    dequed_values.rotate(1)

    return dict(zip(shift.keys(), dequed_values))


def jenny_check(shift):
    """Check value of JK or MW and return True if equal to Jenny"""

    if (
        "JK" in shift
        and shift.get("JK") == "Jenny"
        or "MW, TA, SF" in shift
        and shift.get("MW, TA, SF") == "Jenny"
        or "MW, TA" in shift
        and shift.get("MW, TA") == "Jenny"
    ):
        return True
    else:
        return False
