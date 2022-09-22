from random import shuffle
from time import sleep
from collections import deque
import json

def export(FM, EM):
    """Export results to txt-file"""
    whole_day = {"FM": FM, "EM": EM}
    with open('dagens.txt', 'w') as out_file:
        json.dump(whole_day, out_file, indent = 4, ensure_ascii = False)

def jenny_check(shift):
    """Check value of JK and rotate accordingly"""

    if (len(shift)) == 3:
        que_number = -1
    else:
        que_number = 1

    if shift.get("JK") == "Jenny":
        dequed_values = deque(shift.values())
        dequed_values.rotate(que_number)
        return dict(zip(shift.keys(), dequed_values))
    else:
        return shift


def assignment(slots, workers):
    """This script assigns workers to shifts"""

    workers = [i.capitalize() for i in workers]
    shuffle(workers)
    FM = dict(zip(slots, workers))

    FM = jenny_check(FM)

    dequed_workers = deque(workers)
    dequed_workers.rotate(1)

    EM = dict(zip(slots, list(dequed_workers)))

    EM = jenny_check(EM)

    return FM, EM


def worker_names(num_workers):
    """Ask for names of personel"""

    names = []
    for i in range(num_workers):
        print("-" * 14)
        name = input("Skriv ett namn och tryck enter: ")
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

    num_workers = input("Ange 3 eller 4: ")

    if num_workers == "3":
        FM, EM = three_workers()

    elif num_workers == "4":
        FM, EM = four_workers()

    else:
        print("Försök igen")
        sleep(3)
        menu()

    print("-" * 14)
    print("Morgonen:")
    print(json.dumps(FM, indent=4))
    print("-" * 14)
    print("Eftermiddagen:")
    print(json.dumps(EM, indent=4))
    
    to_print = input("Om du vill skriva schemat till en fil, skriv EXPORT: ")
    
    if to_print == "EXPORT":
        export(FM, EM)
    else: 
        print("Avslutar...")
        sleep(3)

    return FM, EM


def main():
    """Call menu when script runs"""

    FM, EM = menu()

    print(json.dumps(FM, indent=4))
    print(json.dumps(EM, indent=4))
    menu()
    sleep(200)


if __name__ == "__main__":
    main()
