import time
import os

while True:
    now = time.gmtime()
    print(f"{now[3]}:{now[4]}:{now[5]}")
    time.sleep(0.5)
    os.system("clear")