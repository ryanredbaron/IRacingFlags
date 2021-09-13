# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:13:15 2021

@author: ryanr
"""


import time
from enum import Enum
import sys

import irsdk as irsdk
ir = irsdk.IRSDK()
ir.startup()


import tkinter as tk
from PIL import ImageTk, Image
imagepath = r'C:\Users\ryanr\Desktop\Flags\green.jpg'


import threading


class IRacingMemoryFlagType(Enum):
    checkered = 0x0001
    white = 0x0002
    green = 0x0004
    yellow = 0x0008
    red = 0x0010
    blue = 0x0020
    debris = 0x0040
    crossed = 0x0080
    yellow_waving = 0x0100
    one_lap_to_green = 0x0200
    green_held = 0x0400
    ten_to_go = 0x0800
    five_to_go = 0x1000
    random_waving = 0x2000
    caution = 0x4000
    caution_waving = 0x8000
    black = 0x010000
    disqualify = 0x020000
    servicible = 0x040000
    furled = 0x080000
    repair = 0x100000
    start_hidden = 0x10000000
    start_ready = 0x20000000
    start_set = 0x40000000
    start_go = 0x80000000
    

class App(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.imagepath = r'C:\Users\ryanr\Desktop\Flags\green.jpg'
        self.start()

    def callback(self):
        self.root.quit()
        
    def run(self):
        self.root = tk.Tk()
        self.root.title("Join")
        self.root.configure(background='grey')
        self.img = ImageTk.PhotoImage(Image.open(self.imagepath))
        self.panel = tk.Label(self.root, image = self.img)
        self.panel.pack(side = "bottom", fill = "both", expand = "no")
        self.root.mainloop()
        
    def showData(self,imagepathpass):
        img2 = ImageTk.PhotoImage(Image.open(imagepathpass))
        self.panel.configure(image=img2)
        self.panel.image = img2

app = App()

try:
    while(True):
        time.sleep(.25)
        memory_flags = []
        session_flag = ir['SessionFlags']
        if session_flag:
            for flag in IRacingMemoryFlagType:
                if IRacingMemoryFlagType(flag).value & session_flag == IRacingMemoryFlagType(flag).value:
                    memory_flags.append(flag)
            if IRacingMemoryFlagType.blue in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\blue.jpg')
                continue
            if IRacingMemoryFlagType.repair in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\meatball.jpg')
                continue
            if IRacingMemoryFlagType.black in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\black.jpg')
                continue
            if IRacingMemoryFlagType.yellow in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\yellow.jpg')
                continue
            if IRacingMemoryFlagType.green in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\green.jpg')
                continue
            if IRacingMemoryFlagType.white in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\white.jpg')
                continue
            if IRacingMemoryFlagType.checkered in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\checkered.jpg')
                continue
            if IRacingMemoryFlagType.red in memory_flags:
                app.showData(r'C:\Users\ryanr\Desktop\Flags\red.jpg')
                continue
            app.showData(r'C:\Users\ryanr\Desktop\Flags\green.jpg')
        else:
            app.showData(r'C:\Users\ryanr\Desktop\Flags\green.jpg')
        
except (KeyboardInterrupt, SystemExit):
    app.root.quit()
    sys.exit()




