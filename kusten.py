from assign import Workday
from support import names, export
from time import sleep


def main():

    four = ["AJ", "AH, SG", "RO, UA, AHA", "MW, TA, SF"]
    five = ["AJ", "MW, TA", "RO, UA", "AH, SG", "AHA, SF"]

    print("Hur många personal vill du fördela?\n")
    num_names = input("Ange 4 eller 5: ")

    if num_names == "4":
        workers = names(4)
        slots = four
    elif num_names == "5":
        workers = names(5)
        slots = five
    else:
        main()

    kusten = Workday("kusten")
    kusten.assign_workers(workers, slots)

    print(kusten.__repr__())

    to_export = input("Vill du skriva resultatet till en fil? (y/n)")

    if to_export == "y":
        export(kusten)

    else:
        print("Avslutar...")
        sleep(3)
