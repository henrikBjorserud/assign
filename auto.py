from random import shuffle
from time import sleep


def true_shuffle(some_list):
    randomized_list = some_list[:]
    while True:
        random.shuffle(randomized_list)
        for a, b in zip(some_list, randomized_list):
            if a == b:
                break
            else:
                return randomized_list


def jenny_check(FM, EM):

    f = FM.get("JK")
    e = EM.get("JK")
    print(f, e)
    if f == "Jenny":
        return True
    elif e == "Jenny":
        return True
    else:
        return False


def worker_names(num_workers):
    names = []
    for i in range(num_workers):
        print("-" * 14)
        name = input("Skriv ett namn och tryck enter:")
        names.append(name)
        print("-" * 14)
        print(f"Tillagda namn: {', ' .join(names)}")
    sleep(2)
    return names


def four_workers():
    slots = ["JK", "MB, AB, AG", "KU, SA", "GL, FB"]
    workers = worker_names(4)
    FM, EM = assignment(slots, workers)

    print(FM, EM)


def three_workers():
    slots = {"JK", "MB, AB, AG", "KU, GL, FB"}
    workers = worker_names(3)
    FM, EM = assignment(slots, workers)
    print(FM, EM)


def assignment(slots, workers):

    workers = [i.capitalize() for i in workers]

    shuffle(workers)
    FM = dict(zip(slots, workers))

    shuffled_workers = true_shuffle(workers)

    EM = dict(zip(slots, shuffled_workers))

    if jenny_check(FM, EM) == True:
        assignment(slots, workers)

    else:
        return FM, EM


def menu():
    print("Hur många personal jobbar på Verkstan idag?\n")

    num_workers = input("Ange en siffra mellan tre och fyra:")

    if num_workers == "3":
        three_workers()

    elif num_workers == "4":
        four_workers()

    else:
        print("Försök igen")
        sleep(3)
        menu()


def main():

    menu()


if __name__ == "__main__":
    main()
