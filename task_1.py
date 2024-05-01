import datetime

def get_days_from_today(date: str) -> int:
    
    try:
        given_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        today = datetime.date.today()
        delta = today - given_date.date()
        return delta.days
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")
    
print(get_days_from_today("1999-05-09"))