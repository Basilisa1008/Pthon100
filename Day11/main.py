
# 525,600 minutes 
# 60 seconds = 1 minute

# 60 minutes = 1 hour

# 24 hours = 1 day

# 31 days = 1 month

# 12 months = 1 year

# 365 days = 1 year

# 366 day = 1 leap year (this is every four years)

days_this_year = int(input("How many days are in this year?"))

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60


result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute


if days_this_year == 366:
  print("Number of seconds in a leap year are", leapyear_result)
else:
  print("Number of seconds in a year are", result)