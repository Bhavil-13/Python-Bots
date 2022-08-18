import shutil
import psutil
import os
import time
import cv2 as cv

# This program will restart your PC if the free space and disk usage crosses a threshold. You are free to change the 
# Threshold

def restart():
    return os.system("shutdown /r /t 1")

def check_disk_usage(disk):
    Usage = shutil.disk_usage(disk)
    Free_Space = (Usage.free / Usage.total)*100
    return Free_Space < 40

def check_cpu_usage():
    Usage = psutil.cpu_percent(1)
    return Usage > 60

# This program will wait for 10 seconds, then it will show are restarting image and then it will again wait for 10
# seconds and will again wait for 10 seconds and then it will restart the computer.
if check_cpu_usage() and check_disk_usage("/") :
    print("Warning less space and dist in high usage")
    time.sleep(20)
    img = cv.imread('restart.jpg')
    cv.imshow('reset', img)
    cv.waitKey(0)
    restart()
else :
    print("Your System is healthy")