import time
import os
import threading
import keyboard



def set_clock(timer):
    time.sleep(0.1)
    while not keyboard.is_pressed("enter"):
        time.sleep(0.09)
        os.system("clear")
        if keyboard.is_pressed("up"):
            timer = timer + 1
        if keyboard.is_pressed("down"):
            timer = timer - 1
        now = time.gmtime(timer)
        print(f"{now[3]}:{now[4]}:{now[5]}")

    return timer



def timer_clock():
    timer = 0
    time_counter = 0
    while True:
        time.sleep(0.1)
        time_counter = time_counter + 1
        if time_counter == 10 : 
            timer = timer + 1
            time_counter = 0
        os.system("clear")
        now = time.gmtime(timer)
        if keyboard.is_pressed("enter"):
            timer = set_clock(timer)
            time_counter =0
        print(f"{now[3]}:{now[4]}:{now[5]}")


timer_clock()

