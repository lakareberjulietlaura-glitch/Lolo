# Name: Lakareber Juliet Laura
# Registration Number: [Enter your registration number]
# Assignment: Fuel Station Daily Sales
# Python 3.9

def load_litres(filename):
    """Load daily litres sold from a text file and return them as a list."""
    litres = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line != "":
                    litres.append(int(line))

    except FileNotFoundError:
        print("Dataset not found: " + filename)
        return []

    return litres


def total_sales(litres):
    """Return the total litres sold."""
    if len(litres) == 0:
        return 0
    return sum(litres)


def quiet_days(litres, limit=400):
    """Count days when sales were strictly below the given limit."""
    count = 0

    for amount in litres:
        if amount < limit:
            count += 1

    return count


def create_report(litres):
    """Create and return the fuel station summary as text."""
    days_recorded = len(litres)
    total = total_sales(litres)
    average = total / days_recorded
    busiest_day = max(litres)
    quiet = quiet_days(litres)

    report = (
        "===== FUEL STATION SUMMARY =====\n"
        f"Days recorded:     {days_recorded}\n"
        f"Total litres:      {total}\n"
        f"Average per day:   {average:.1f}\n"
        f"Busiest day:       {busiest_day} litres\n"
        f"Quiet days (<400): {quiet}"
    )

    return report


def main():
    filename = "litres.txt"
    litres = load_litres(filename)

    if len(litres) == 0:
        print("No data to analyse.")
    else:
        report = create_report(litres)
        print(report)

        with open("station_report.txt", "w") as file:
            file.write(report + "\n")

        print("Report saved to station_report.txt")


if __name__ == "__main__":
    main()
