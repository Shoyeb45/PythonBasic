# Create a python program capable of greeting you with Good Morning, Good Afternoon and 
# Good Evening. Your program should use time module to get the current hour.

import time

currentTime = int(time.strftime('%H'))

if(currentTime>=5 and currentTime<12):
    print("Good Morning...")
elif(currentTime>=12 and currentTime<18):
    print("Good Afternoon...")
else:
    print("Good Evening...")

