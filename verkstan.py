from assign import Workday
from support import names, export
from time import sleep


def main():

    three = ["JK", "MB, AB, AG", "KU, GL, FB"]
    four = ["JK", "MB, AB, AG", "KU, SA", "GL, FB"]

    print("Hur många personal vill du fördela?\n")
    num_names = input("Ange 3 eller 4: ")

    if num_names == "3":
        workers = names(3)
        slots = three
    elif num_names == "4":
        workers = names(4)
        slots = four
    else:
        main()

    verkstan = Workday("verkstan")
    verkstan.assign_workers(workers, slots)

    print(verkstan.__repr__())

    to_export = input("Vill du skriva resultatet till en fil? (y/n)")

    if to_export == "y":
        export(verkstan)

    else:
        print("Avslutar...")
        sleep(3)


if __name__ == "__main__":
    main()
