from datetime import datetime, timedelta

# 1. Date Utility Functions

def days_until(date_str: str) -> int:
    """
    Takes a date string in "YYYY-MM-DD" format and returns the 
    number of days from today (local time) to that date.
    """
    target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    today = datetime.now().date()
    return (target_date - today).days


def is_business_day(d: datetime.date) -> bool:
    """
    Returns True if the given date falls on Monday through Friday, 
    and False if it falls on Saturday or Sunday.
    """
    return d.weekday() < 5


def next_business_day() -> datetime.date:
    """
    Returns tomorrow if tomorrow is a business day.
    Otherwise, skips to the upcoming Monday.
    """
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    
    # If tomorrow is Saturday (5), add 2 days to get to Monday
    if tomorrow.weekday() == 5:
        return tomorrow + timedelta(days=2)
    # If tomorrow is Sunday (6), add 1 day to get to Monday
    elif tomorrow.weekday() == 6:
        return tomorrow + timedelta(days=1)
    
    return tomorrow

# 2. Testing and Demonstration

if __name__ == "__main__":
    print("--- Running Date Utility Tests ---")
    
    # Current reference point
    today_date = datetime.now().date()
    print(f"Today's Date: {today_date} ({today_date.strftime('%A')})\n")
    
    # Test (a): days_until
    target = "2026-12-31"
    days_left = days_until(target)
    print(f"Test (a): days_until('{target}')")
    print(f"  -> Days remaining: {days_left} days\n")
    
    # Test (b): is_business_day
    # Let's test today, a known Saturday, and a known Sunday
    test_weekday = datetime(2026, 7, 15).date()  # Wednesday
    test_weekend = datetime(2026, 7, 19).date()  # Sunday
    
    print("Test (b): is_business_day(d)")
    print(f"  -> {test_weekday} ({test_weekday.strftime('%A')}): {is_business_day(test_weekday)}")
    print(f"  -> {test_weekend} ({test_weekend.strftime('%A')}): {is_business_day(test_weekend)}")
    print(f"  -> Today ({today_date.strftime('%A')}): {is_business_day(today_date)}\n")
    
    # Test (c): next_business_day
    next_biz = next_business_day()
    print("Test (c): next_business_day()")
    print(f"  -> Next business day is: {next_biz} ({next_biz.strftime('%A')})")