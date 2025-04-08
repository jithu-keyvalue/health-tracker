def print_chart(history):
    print("\nYour Hb trend:")
    for date, hb in history.items():
        bars = "▓" * int(hb * 2)
        print(f"{date} | {bars:<20} {hb}")
