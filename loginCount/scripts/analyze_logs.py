import sys
from datetime import datetime
from datetime import date, timedelta
import subprocess


def parse_date(date_str):
    """Parses a date string in YYYY-MM-DD format and returns a datetime object.

    Args:
        date_str: The date string in YYYY-MM-DD format.

    Returns:
        A datetime object representing the parsed date, or None if parsing fails.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None


def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <start_date> <end_date>")
        sys.exit(1)

    start_date = parse_date(sys.argv[1])
    end_date = parse_date(sys.argv[2])

    if not start_date or not end_date:
        sys.exit(1)  # Exit if parsing failed

    for day in range((end_date - start_date).days + 1):
        current_date = start_date + timedelta(days=day)
        current_date_plus_1 = current_date + timedelta(days=1)
        current_date_as_str = current_date.strftime("%Y-%m-%d")
        current_date_plus_1_as_str = current_date_plus_1.strftime("%Y-%m-%d")

        command = f"journalctl --since {current_date_as_str} --until {current_date_plus_1_as_str} | grep systemd-logind | grep -i 'new' > logins_{current_date_as_str}"

        # Execute the command using subprocess
        process = subprocess.run(command, shell=True, capture_output=True)

        # Check the return code
        if process.returncode == 0:
            print("Command successful")
        else:
            print(f"Error running command (code: {process.returncode})")
            print(f"Output: {process.stdout.decode()}")  # Print command output (optional)

        print(command)


if __name__ == "__main__":
    main()

