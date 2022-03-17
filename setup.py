import os
import time

os.system("pip install --upgrade --force-reinstall pytube")
print("Setup done")
t = 4
while t:
    mins, secs = divmod(t, 60) 
    timer = 'Closing in {:02d}:{:02d}'.format(mins, secs) 
    print(timer, end="\r") 
    time.sleep(1) 
    t -= 1
