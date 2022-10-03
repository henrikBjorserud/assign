import json


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

    return worker_names


def export(schedule):
    """Export results to txt-file"""
    with open("dagens.txt", "w") as out_file:
        json.dump(schedule.__dict__, out_file, indent=4, ensure_ascii=False)

    return "Schedule Exported"
