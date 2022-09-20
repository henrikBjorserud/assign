from random import shuffle
from time import sleep
from collections import deque
import json


def assignment(slots, workers):
    
    workers = [i.capitalize() for i in workers]
    shuffle(workers)
    FM = dict(zip(slots, workers))
    

    dequed_workers = deque(workers)
    dequed_workers.rotate(1)
    EM = dict(zip(slots, list(dequed_workers)))
    
    return FM, EM


def worker_names(num_workers):
    
    names = []
    for i in range(num_workers):
        print("-" * 14)
        name = input("Skriv ett namn och tryck enter:")
        names.append(name)
        print("-" * 14)
        print(f"Tillagda namn: {', ' .join(names)}")

    return names


def four_workers():
    slots = ["JK", "MB, AB, AG", "KU, SA", "GL, FB"]
    workers = worker_names(4)
    FM, EM = assignment(slots, workers)

    return FM, EM


def three_workers():
    slots = {"JK", "MB, AB, AG", "KU, GL, FB"}
    workers = worker_names(3)
    FM, EM = assignment(slots, workers)
    return FM, EM


def menu():
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
    
    print(json.dumps(FM, indent=4))
    print(json.dumps(EM, indent=4))

def main():

    menu()


if __name__ == "__main__":
    main()
