# Example 11

import csv

DATE_INDEX = 0
START_MILES_INDEX = 1
END_MILES_INDEX = 2
GALLONS_INDEX = 3


def main():
    try:
        # Open the fuel_usage.csv file.
        filename = "fuel_usage.csv"
        with open(filename, "rt") as usage_file:

            # Use the standard csv module to get
            # a reader object for the CSV file.
            reader = csv.reader(usage_file)

            # The first line of the CSV file contains headings
            # and not fuel usage data, so this statement skips
            # the first line of the CSV file.
            next(reader)

            # Print headers for the three columns.
            print("Date,Start,End,Gallons,Miles/Gallon")

            # Process each row in the CSV file.
            for row in reader:

                # From the current row of the CSV file, get
                # the date, the starting and ending odometer
                # readings, and the number of gallons used.
                date = row[DATE_INDEX]
                start_miles = float(row[START_MILES_INDEX])
                end_miles = float(row[END_MILES_INDEX])
                gallons = float(row[GALLONS_INDEX])

                # Call the miles_per_gallon function.
                mpg = miles_per_gallon(start_miles, end_miles, gallons)

                # Display the results for one row.
                mpg = round(mpg, 1)
                print(date, start_miles, end_miles, gallons, mpg,
                        sep=",")

    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                " because it doesn't exist.")

    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                " because you don't have permission.")

    except ZeroDivisionError as zero_div_err:
        print(f"Error: {filename} contains a"
                " zero in the gallons column.")


def miles_per_gallon(start_miles, end_miles, gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    start_miles and end_miles are odometer readings in miles.
    gallons is a fuel amount in U.S. gallons.
    """
    mpg = abs(end_miles - start_miles) / gallons
    return mpg


# Call main to start this program.
if __name__ == "__main__":
    main()