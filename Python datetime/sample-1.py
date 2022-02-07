import datetime

###################################
#### Create a date/time/datetime object
###################################

# Create a date object from year, month, day
d1 = datetime.date(2022,12,24)
print(d1) # output: 2022-12-24

# Create a date object of today
d2 = datetime.date.today()
print(d2) # output: 2022-02-07 (i.e. the date of today)

# Create a time object from hour, minute, second, microsecond
t1 = datetime.time(9,10,20,1000)
print(t1) # output: 09:10:20.001000 

# Create a datetime object from year, month, day, hour, minute, second, microsecond
dt1 = datetime.datetime(2022,1,19,18,10,5,40000) 
print(dt1) # output: 2022-01-19 18:10:05.040000

# Create a datetime object of now
dt2 = datetime.datetime.now()
print(dt2) # output: 2022-02-07 12:19:47.232704 (i.e. now )

###################################
#### Component of date/time/datetime object
###################################

# Component of date object
# d1 = 2022-12-24
print(d1.year) # output: 2022
print(d1.month) # output: 12
print(d1.day) # output: 24

# Component of time object
# t1 = 09:10:20.001000
print(t1.hour) # output: 9
print(t1.minute) # output: 10
print(t1.second) # output: 20
print(t1.microsecond) # output: 1000

# Component of time object
# dt1 = 2022-01-19 18:10:05.040000
print(dt1.year) # output: 2022
print(dt1.month) # output: 1
print(dt1.day) # output: 19
print(dt1.hour) # output: 18
print(dt1.minute) # output: 10
print(dt1.second) # output: 5
print(dt1.microsecond) # output: 40000

# Date / time portion of a datetime
# dt1 = 2022-01-19 18:10:05.040000
print(dt1.date()) # output: 2022-01-19
print(dt1.time()) # output: 18:10:05.040000

###################################
### Time delta
###################################

# Define a time delta
# one week + 2 days + 3 minutes + 4 seconds
tdelta1 = datetime.timedelta(weeks=1, days=2, minutes=3, seconds=4)
print(tdelta1) # output: 9 days, 0:03:04

# datetime move forward by time delta
# dt1 = 2022-01-19 18:10:05.040000
# tdelta1 = 9 days, 0:03:04
print(dt1 + tdelta1) # output : 2022-01-28 18:13:09.040000

# datetime move backwards by time delta
# dt1 = 2022-01-19 18:10:05.040000
# tdelta1 = 9 days, 0:03:04
print(dt1 - tdelta1) # output : 2022-01-10 18:07:01.040000

# calculate the time difference of 2 dates/times/datetimes
d2a = datetime.date(2019,10,10)
d2b = datetime.date(2020,1,1)
print(d2a - d2b) # output: -83 days, 0:00:00
dt2a = datetime.datetime(2019,10,10,15,10,0)
dt2b = datetime.datetime(2019,10,9,12,11)
print(dt2a - dt2b) # output: 1 day, 2:59:00

###################################
### Day of Week
###################################
# d1 = 2022-12-24
# Day of Week : 0 = MON, 6 = SUN
print(d1.weekday())     # Output = 5
# Iso Day of week : 1 = MON, 7 = SUN
print(d1.isoweekday())  # Output = 6


##################################
# pytz
##################################
import pytz

# UTC format
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)  # output : 2022-02-07 12:21:36.906308+00:00

#print(pytz.all_timezones)
# Convert the local time to another timezone
dt3 = datetime.datetime(2000,10,10,1,2,3)
dt3_hkutc = dt3.astimezone(pytz.timezone('Asia/Hong_Kong'))
print(dt3_hkutc) # output : 2000-10-10 08:02:03+08:00

######################################
# Convert String to datetime or vice versa
######################################
# dt3 : 2000-10-10 01:02:03
print(dt3.strftime('%B %d, %Y %H:%M:%S')) # Output : October 10, 2000 01:02:03

dt4_str = 'July 26, 2014'
dt4 = datetime.datetime.strptime(dt4_str, '%B %d, %Y') # Output : 2014-07-26 00:00:00
print(dt4)