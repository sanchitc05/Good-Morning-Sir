Name = input("Enter your name: ")
Gen = input("Enter your gender : ")

Gen = Gen.lower()
import time
timestamp = int(time.strftime('%H'))


if timestamp < 12:
    greeting = "Good Morning"
elif 12 <= timestamp < 17:
    greeting = "Good Afternoon"
elif 17 <= timestamp < 21:
    greeting = "Good Evening"
else:
    greeting = "Good Night"

if Gen == "male":
    title = "Sir"

elif Gen == "female":
    title = "Ma'am"

else: 
    title = ""

print(f"{greeting}, {Name} {title}")
