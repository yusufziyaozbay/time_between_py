# Calculate the difference between two selected times

# Get the user input
time_input1 = input('Enter first time input (--:--): ')
time_input2 = input('2nd input (--:--): ')

# Split times to hour and minute
time_input_parts1 = time_input1.split(':')
time_input_parts2 = time_input2.split(':')

time1_hour = int(time_input_parts1[0])
time2_hour = int(time_input_parts2[0])

time1_minute = int(time_input_parts1[1])
time2_minute = int(time_input_parts2[1])

# Calculate
if time1_minute > time2_minute:
    minute = (60 - time1_minute) + time2_minute
    hour = abs((time1_hour - time2_hour)) - 1
else:
    minute = abs(time2_minute - time1_minute)
    hour = abs(time1_hour - time2_hour)

print(f'Time1 - Time2 = {hour}:{minute}')
# update test