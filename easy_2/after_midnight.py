# Input – a number of minutes
# Output – the time of day in hh:mm format
# Should work wit any integer, including those that are more than or less than one day

# Input is an integer, output is a string
# Calculate hours by doing integer division
# Calculate leftover minutes by subtracting hours * 60
# The remainder of hours divided by 24 will provide the 'net distance' in hours
# Then just add the minutes

# def time_of_day(integer):
#     hours = (integer // 60)
#     minutes = integer - (hours * 60)
#     hours_added = hours % 24
#     time = str(f'{hours_added}:{minutes}')
#     return time

# print(time_of_day(-4231))

time = "12:34"

MINUTES_IN_HOUR = 60
MINUTES_IN_DAY = 1440
def after_midnight(string):
    hours = int(string[0:2])
    minutes = int(string[3:5])
    total = (hours * MINUTES_IN_HOUR) + minutes
    while total >= MINUTES_IN_DAY:
        total -= MINUTES_IN_DAY
    return total

def before_midnight(string):
    hours = int(string[0:2])
    minutes = int(string[3:5])
    total = (hours * MINUTES_IN_HOUR) + minutes
    while total >= MINUTES_IN_DAY:
        total -= MINUTES_IN_DAY
    before_total = MINUTES_IN_DAY - total
    return before_total

print(before_midnight(time))