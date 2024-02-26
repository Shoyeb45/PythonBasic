import sys
import math
try:
    x = 5
    y = 0
    result = x/y
    print(result)
except:
    excType, excValue, excTracebak = sys.exc_info()
    print(f"Some error happened {excType}")

try:
    x = -25
    y = 0
    result = math.sqrt(x)
    print(result)
except Exception as o:
    print(f"Some error happened {o}")