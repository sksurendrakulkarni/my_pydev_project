'''
Created on Feb 4, 2020

@author: sksurendrakulkarni

import pygame
pygame.init()

clock = pygame.time.Clock()

while True:
    clock.tick(30)


import time

FPS = 30

last_time = time.time()

while True:
    new_time = time.time()
    sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
    if sleep_time > 0:
        time.sleep(sleep_time)
    last_time = new_time
'''
import time
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


#root = Tk()
#time1 = ''

def tick(time1=''):
    #global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text = time2)
    clock.after(200, tick)

root = tk.Tk()
clock = tk.Label(root, font=('times',20,'bold'), bg = 'green')
clock.pack(fill='both', expand=1)
tick()
root.mainloop( )

if __name__ == '__main__':
    print('Hello World')