from assign import Workday
from support import names, export
import json
from time import sleep


def main():

    three = ["JK", "MB, AB, AG", "KU, GL, FB"]
    four = ["JK", "MB, AB, AG", "KU, SA", "GL, FB"]


    print("Hur många personal vill du fördela?\n")
    num_names = input("Ange 3 eller 4: ")

    if num_names == "3":
        workers = names(3)
        slots = three
    else:
        workers = names(4)
        slots = four
    
    print(workers, slots)
    verkstan = Workday("verkstan")
    verkstan.assign_workers(workers, slots)
    print("-" * 14)
    print("Morgonen:")
    print(verkstan.before_lunch)
    print("-" * 14)
    print("Eftermiddagen:")
    print(verkstan.after_lunch)

    to_export = input("Vill du skriva resultatet till en fil? (y/n)")

    if to_export == "y":
        export(schedule)

    else:
        print("Avslutar...")
        sleep(3)


if __name__ == "__main__":
    main()
