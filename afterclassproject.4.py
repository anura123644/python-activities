import calendar

# Get the list of month names
months = list(calendar.month_name)

# Remove the first element which is an empty string
months = months[1:]

# Display the month names
for month in months:
    print(month)
