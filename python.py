a = input("Enter your name: ")

import time
timestamp = time.strftime('%H')
if int(timestamp) < 12:
  print("Good Morning", a)
elif int(timestamp) > 12 and int(timestamp) < 17:
  print("Good Afternoon", a)
elif int(timestamp) > 17 and int(timestamp) < 23:
  print("Good Evening", a)
else:
  print("Good night", a)
