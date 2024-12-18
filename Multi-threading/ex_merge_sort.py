import threading 
import time 

def mergeSort(listNum: list) -> list:
    if len(listNum) == 1:
        return listNum
    
    