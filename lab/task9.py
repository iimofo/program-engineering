from datetime import datetime as dt
from datetime import timedelta as td

def calculate_future_day():
    today = dt.now()
    print(f"Today's date: {today.date()}")
    print(f"Day of the week (1=Mon, 7=Sun): {today.isoweekday()}")
    try:
        n = int(input('\nEnter the number of days: '))
        days_to_add = td(days=n)
        future_date = today + days_to_add
        print(f"\nAfter {n} days, the date will be: {future_date.date()}")
        print(f"The day of the week (1=Mon, 7=Sun) will be: {future_date.isoweekday()}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

if __name__ == '__main__':
    calculate_future_day()