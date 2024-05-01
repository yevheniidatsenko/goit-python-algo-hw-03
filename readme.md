## Homeworks #4: Working with dates, time and advanced string operations

**Skills you will gain by completing the tasks:**

- Calculate the number of days between a given date and the current date.
- Generate a set of unique random numbers within the specified parameters.
- Normalize phone numbers to standard format.
- Output a list of colleagues' birthdays for a week ahead.

**Task 1: Days between dates**

- Create a function `get_days_from_today(date)` that calculates the number of days between a given date and today.
- The function takes one parameter: `date` - a string representing a date in 'YYYY-MM-DD' format.
- The function returns an integer representing the number of days between the given date and today.
- If the given date is in the future, the result should be negative.
- Use the `datetime` module for date calculations.

**Task 2: Lottery ticket generator**

- Create a function `get_numbers_ticket(min, max, quantity)` that helps generate random unique number sets for lottery tickets.
- The function takes three parameters:
  - `min` - the minimum possible number in the set (no less than 1).
  - `max` - the maximum possible number in the set (no more than 1000).
  - `quantity` - the number of numbers to choose (a value between `min` and `max`).
- The function generates the specified number of unique random numbers within the given range.
- The function returns a sorted list of randomly chosen numbers.
- If the parameters do not meet the specified requirements, the function returns an empty list.

**Task 3: Phone number normalizer**

- Create a function `normalize_phone(phone_number)` that normalizes phone numbers to a standard format.
- The function takes one argument - a string with a phone number in any format.
- The function removes all characters except digits and the '+' symbol.
- If the international code is missing, the function adds the '+38' code (for Ukraine).
- The function returns the normalized phone number as a string.

**Task 4: Upcoming birthdays**

- Create a function `get_upcoming_birthdays(users)` that helps identify colleagues whose birthdays are coming up.
- The function takes one parameter: `users` - a list of dictionaries, where each dictionary contains keys `name` (user's name, string) and `birthday` (birthday in 'YYYY.MM.DD' format).
- The function should determine who has birthdays within the next 7 days (including today).
- If a birthday falls on a weekend, the greeting date should be moved to the next Monday.
- The function returns a list of dictionaries, where each dictionary contains information about the user (key `name`) and the greeting date (key `congratulation_date`, formatted as 'YYYY.MM.DD').
