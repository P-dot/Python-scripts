#!/usr/bin/env python

import pygtk, gtk
pygtk.require("2.0")

class Timer():
   def _init_(self):
       self.x = 0
       self.Win()

   def Win(self):
       self.win = gtk.Window()
       self.win.connect("destory", lambda q: gtk.main_quit())
       self.box1 = gtk.HBox()
       self.win.add(self.box1)
       self.box1.show()
       
       self.label = gtk.Label(self.x)
       self.box1.pack_start(self.label)
       self.label.show()

       self.button1 = gtk.Button("Start")
       self.box1.pack_start(self.button1)

