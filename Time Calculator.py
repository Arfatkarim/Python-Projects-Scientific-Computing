def add_time(start, duration, day_of_week=None):
    # Days of the week in order
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Split start time into components
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start time to 24-hour format
    if period.upper() == "PM" and start_hour != 12:
        start_hour += 12
    if period.upper() == "AM" and start_hour == 12:
        start_hour = 0

    # Split duration into hours and minutes
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add minutes and handle overflow
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    # Add hours
    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_period = "PM"

    # Format minutes with leading zero if needed
    final_minute_str = str(final_minute).rjust(2, '0')

    # Calculate new day of the week if given
    if day_of_week:
        day_index = days.index(day_of_week.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days[new_day_index]
        day_part = f", {new_day}"
    else:
        day_part = ""

    # Handle day notation
    if days_later == 1:
        days_later_part = " (next day)"
    elif days_later > 1:
        days_later_part = f" ({days_later} days later)"
    else:
        days_later_part = ""

    # Combine final result
    new_time = f"{final_hour}:{final_minute_str} {final_period}{day_part}{days_later_part}"
    return new_time

# Example usages:
print(add_time('3:00 PM', '3:10'))                       # 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))           # 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))                    # 12:03 PM
print(add_time('10:10 PM', '3:30'))                     # 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))        # 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))                    # 7:42 AM (9 days later)