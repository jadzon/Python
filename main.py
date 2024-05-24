from abc import ABC, abstractmethod
import msvcrt
import os
from Models.puma_model import Puma

def clear_input_buffer():
    try:
        while True:
            input()
    except EOFError:
        pass  # End of file reached
#Nie wiem co to robi ale dziala
def non_blocking_input():
    if os.name == 'nt':  # Windows
        return msvcrt.getch().decode()
    else:  # Unix-like
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

puma_robot = Puma()
while True:
    move = non_blocking_input()
    if move == 'w':
        print('w')
        puma_robot.p2_spin_forward()
        puma_robot.show_positions()
    elif move =='s':
        print('s')
        puma_robot.p2_spin_backward()
        puma_robot.show_positions()
    elif move =='a':
        print('a')
        puma_robot.p1_spin_left()
        puma_robot.show_positions()
    elif move =='d':
        print('d')
        puma_robot.p1_spin_right()
        puma_robot.show_positions()
    elif move == 'l':
        break
    elif move == 'k':
        puma_robot.p3_spin_backward()
        puma_robot.show_positions()
    elif move == 'i':
        puma_robot.p3_spin_forward()
        puma_robot.show_positions()