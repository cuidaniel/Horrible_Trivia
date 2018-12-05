#!/usr/bin/env python
import tkinter as tk
import sys
import random
import termios
import os

needAnswer = False;
question = "";

def progress():
	 return lambda : callback();

def callback():
	global question;
	global needAnswer;
	if needAnswer == False:
		question = random.choice(list(questionHolder.keys()));
		tex.insert(tk.END, question+"\n")
		tex.see(tk.END)			 # Scroll if necessary
		needAnswer = True;
	else:
		needAnswer = False;
		tex.insert(tk.END, questionHolder[question]+"\n\n")
		tex.see(tk.END)			 # Scroll if necessary

questionFile = open("Trivia_Questions.csv");
questionHolder = {};
count = 0;
for line in questionFile:
	count +=1;
	q,a = line.strip().split(",,");
	questionHolder[q] = a;
questionFile.close();

top = tk.Tk()
tex = tk.Text(master=top,wrap="word")
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
tk.Button(bop, text="Click Here", command=progress()).pack()

tk.Button(bop, text='Exit', command=top.destroy).pack()

tex.insert(tk.END, "Dan\'s shitty trivia thing.\n\n")
tex.see(tk.END)			 # Scroll if necessary

top.mainloop()