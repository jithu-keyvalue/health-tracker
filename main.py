from validation import get_name, get_date, get_hb
from storage import load_from_csv, save_to_csv

def collect_history():
    count = int(input("How many Hb records do you want to enter? "))
    history = {}

    for _ in range(count):
        date = get_date()
        hb = get_hb()
        history[date] = hb

    return history


def main():
    print("Welcome to Health Tracker!")
    name = get_name()
    filename = f"{name.lower()}.csv"

    history = load_from_csv(filename)
    new_entries = collect_history()
    history.update(new_entries)
    history = dict(sorted(history.items()))

    print(f"\nHi {name}, here is your updated Hb history:")
    print_chart(history)

    save_to_csv(history, filename)


main()
