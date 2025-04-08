def load_from_csv(filename):
    history = {}

    try:
        with open(filename, "r") as file:
            next(file)
            for line in file:
                line = line.strip()
                if not line:
                    continue
                date, hb = line.split(",")
                history[date] = float(hb)
    except FileNotFoundError:
        pass

    return history


def save_to_csv(history, filename):
    with open(filename, "w") as file:
        file.write("date,hb\n")
        for date, hb in history.items():
            file.write(f"{date},{hb}\n")
    print("\nSaved data.")
