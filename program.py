def collect_hb_history():
    entry_count = int(input("How many Hb records do you want to enter? "))
    hb_history = {}

    for _ in range(entry_count):
        date = input("Enter date (YYYY-MM-DD): ")
        hb = float(input("Enter Hb value for that date: "))
        hb_history[date] = hb

    return hb_history


def print_hb_chart(hb_history):
    print("\nYour Hb trend:")
    for date, hb in hb_history.items():
        bars = "▓" * int(hb * 2)
        print(f"{date} | {bars:<20} {hb}")


def load_hb_from_csv(filename="hb_data.csv"):
    hb_history = {}

    try:
        with open(filename, "r") as file:
            next(file)  # skip header
            for line in file:
                line = line.strip()
                if not line:
                    continue
                date, hb = line.split(",")
                hb_history[date] = float(hb)
    except FileNotFoundError:
        pass  # first run, no file yet

    return {}


def save_hb_to_csv(hb_history, filename="hb_data.csv"):
    with open(filename, "w") as file:
        file.write("date,hb\n")
        for date, hb in hb_history.items():
            file.write(f"{date},{hb}\n")

    print('\nSaved data.')


def main():
    print("Welcome to Health Tracker!")
    name = input("What is your name? ")

    hb_history = load_hb_from_csv()
    new_entries = collect_hb_history()
    hb_history.update(new_entries)

    # sort by date
    hb_history = dict(sorted(hb_history.items()))

    print(f"\nHi {name},")
    print(hb_history)

    print_hb_chart(hb_history)

    save_hb_to_csv(hb_history)
    

main()
