from datetime import date

def calculate_age(birthdate):
    today = date.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    # check if birthdate is yet to occur this year
    if (months < 0) or (months == 0 and days < 0):
        years -= 1
    # calculate total months and days
    total_months = (years * 12) + abs(months)
    total_days = (today - birthdate).days
    # return age in years, months, and days
    return years, total_months, total_days

# example usage
birthdate = date(1990, 5, 15)
age_years, age_months, age_days = calculate_age(birthdate)
print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")
