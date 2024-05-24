from datetime import *

now = datetime.now()

current_date = date.today()
current_time = now.strftime("%H:%M:%S")
current_hr = now.strftime("%H")

print(current_date)
print(current_time)
print(current_hr)