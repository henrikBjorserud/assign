import assign
from .support import names
from .support import export
from .extras import jennycheck


def main():

    three = ["JK", "MB, AB, AG", "KU, GL, FB"]
    four = ["JK", "MB, AB, AG", "KU, SA", "GL, FB"]

    assign = assign.Assign()

    print("Hur många personal vill du fördela?\n")
    num_names = input("Ange 3 eller 4: ")

    if num_names == "3":
        workers = names(3)
        slots = three
    else:
        workers = names(4)
        slots = four

    schedule = assign(workers, slots)

    print("-" * 14)
    print("Morgonen:")
    print(json.dumps(schedule.get("FM"), indent=4))
    print("-" * 14)
    print("Eftermiddagen:")
    print(json.dumps(schedule.get("EM"), indent=4))

    to_export = input("Vill du skriva resultatet till en fil? (y/n)")

    if to_export == "y":
        export(schedule)

    else:
        print("Avslutar...")
        sleep(3)


if __name__ == "__main__":
    main()
