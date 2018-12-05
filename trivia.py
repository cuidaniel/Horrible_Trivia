#!/usr/bin/env python3

import sys
import random
import termios
import os

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)       
        flush_to_stdout(c)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    if c == b'\x7f': # Backspace/delete is hit
        return "delete"
    return c.decode("utf-8")

def flush_to_stdout(c):
    if c == b'\x7f':
        sys.stdout.write("\b \b")
    else:
        sys.stdout.write(c.decode("utf-8"))
        sys.stdout.flush()

questionFile = open("Trivia_Questions.csv");
questionHolder = {};
count = 0;
for line in questionFile:
    count +=1;
    question,answer = line.strip().split(",,");
    questionHolder[question] = answer;
questionFile.close();

print("Dan\'s shitty trivia thing.");
print("Press space to get the answer/move on to the next question.");
print("Ctrl-C to quit.")

needAnswer = False;
while True:
    key = getkey();
    if key == " ":
        if needAnswer == False:
            q = random.choice(list(questionHolder.keys()));
            print(q);
            needAnswer = True;
        else:
            print(questionHolder[q]);
            needAnswer = False;
