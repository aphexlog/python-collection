from dateutil.tz import tzstr, tzlocal
from datetime import datetime

print("To demonstrate timezone using dateutil module and also used for parsing:")
print("\n")
now = datetime.now()
local = tzlocal()
now = datetime.now()
now = now.replace(tzinfo = tzstr("US/Central"))
now = now.astimezone(local)
now =now.today()
print("Current time in local timezone: ")
print(now)




# print("The local timezone is as follows which is timezone awarew datetime")
# print(now)
# print("\n")
# utc = tzutc()
# cdt = tzstr("US/Central")
# dt = now.astimezone(cdt)
# print("The below is converted utc datetime of the above given local timezone")
# print(dt)

