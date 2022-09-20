from random import shuffle
from time import sleep
from collections import deque
import json


"""This script assigns workers to shifts"""


def assignment(shifts, workers):
    """Assign personel to shifts"""
    workers = [i.capitalize() for i in workers]
    shuffle(workers)
    FM = dict(zip(shifts, workers))

    dequed_workers = deque(workers)
    dequed_workers.rotate(1)
    EM = dict(zip(shifts, list(dequed_workers)))

    return FM, EM


def worker_names(num_workers):
    """Ask for names of personel"""
    names = []
    for i in range(num_workers):
        print("-" * 14)
        name = input("Skriv ett namn och tryck enter:")
        names.append(name)
        print("-" * 14)
        print(f"Tillagda namn: {', ' .join(names)}")

    return names


def four_workers():
    """Establish four shifts"""
    shifts = ["JK", "MB, AB, AG", "KU, SA", "GL, FB"]
    workers = worker_names(4)
    FM, EM = assignment(shifts, workers)

    return FM, EM


def three_workers():
    """Establish three shifts"""
    shifts = {"JK", "MB, AB, AG", "KU, GL, FB"}
    workers = worker_names(3)
    FM, EM = assignment(shifts, workers)
    return FM, EM


def menu():
    """Ask user for number of personel"""

    print("Hur många personal vill du fördela?\n")

    num_workers = input("Ange 3 eller 4:")

    if num_workers == "3":
        FM, EM = three_workers()

    elif num_workers == "4":
        FM, EM = four_workers()

    else:
        print("Försök igen")
        sleep(3)
        menu()

    return FM, EM


def main():
    """Call menu when script runs"""

    FM, EM = menu()

    print(json.dumps(FM, indent=4))
    print(json.dumps(EM, indent=4))


if __name__ == "__main__":
    main()
