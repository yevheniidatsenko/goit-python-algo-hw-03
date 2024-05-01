from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday_this_year < today:
            birthday_next_year = birthday_this_year.replace(year=today.year + 1)
        else:
            birthday_next_year = birthday_this_year

        days_diff = (birthday_next_year - today).days

        if days_diff >= 0 and days_diff <= 7:
            if birthday_next_year.weekday() >= 5:
                congratulation_date = birthday_next_year + timedelta(days=(9 - birthday_next_year.weekday()))
            else:
                congratulation_date = birthday_next_year

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.05.04"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("This week's list of birthday greetings:", upcoming_birthdays)