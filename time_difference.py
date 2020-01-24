# This will calculate the difference between two times in 12 hour format.
# Please enter start time. 
# Please enter end time. 
import datetime
# Record start time and end time
time_in = input("Start time: ")
time_out = input("End time: ")


def get_time(time_str):
	time_str = time_str.replace(" ", "")
	ending = time_str[-2:]
	hour, minute = time_str[:-2].split(":")
	hour = int(hour)
	minute = int(minute)
	if ending == "pm":
		hour += 12
	return [hour, minute]

# This will set up the datetime.datetime
today = datetime.date.today()
year = today.year
month = today.month
day = today.day

# Get the hour and minute for the datetime.datetime
start_hour, start_min = get_time(time_in)
end_hour, end_min = get_time(time_out)

# Create the datetime.datetime to create a timedelta
start_time = datetime.datetime(year, month, day, start_hour, start_min)
end_time = datetime.datetime(year, month, day, end_hour, end_min)

time_diff = (end_time - start_time).total_seconds()
time_diff = round(time_diff/3600,2)
print(f"You worked {time_diff} hours.")