import datetime
import calendar

# Read date from user (format: YYYY-MM-DD)
date_input = input("Enter today's date (YYYY-MM-DD): ")

# Convert string to date object
today = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

# Get total number of days in the month
total_days = calendar.monthrange(today.year, today.month)[1]

# Calculate remaining days
days_left = total_days - today.day

print("Days left in the current month:", days_left)
