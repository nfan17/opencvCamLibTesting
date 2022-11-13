# Main script to test cam module function
# Took out passing current dir as path because had issues getting raspberry pi to read path from arg

from cam import cam
import sys
import numpy as np

def main():
    #dir = rf"{path[1]}"
    dir = "/home/pi/"
    camera = cam(dir)
    with open("/home/pi/commands.txt") as file:
        f = file.readlines()
        seq = f[0].split(":")
        print(seq)
        comms = seq[1].split(" ")
        while len(comms) > 0:
            next = comms.pop(0)
            if next == "A1":
                pass #gimbal 60 deg right
            elif next == "B2":
                pass #gimbal 60 deg left
            elif next == "C3":
                if camera.snapshot(): print(camera) 
                else: print(False)
            elif next == "D4":
                camera.lastState[0] = True 
            elif next == "E5":
                camera.lastState[0] = False
            elif next == "F6":
                camera.lastState[1] = True if not camera.lastState[1] else False
            elif next == "G7":
                camera.lastState[2] = True
            elif next == "H8":
                camera.lastState[2] = False
            elif next == "clear":
                camera.lastState = [False, False, False]  
            elif next == "exit":
                break                
    camera.release()


if __name__ == "__main__":
    main()
