# UPDATE WRITE PATH BEFORE RUNNING CODE!!! - LINE 72, or ctrl+F: path
# Insert the directory in which you will be running the code (also where new photos will save)

import cv2
import datetime
import numpy as np

lastState = np.zeros(3, dtype=bool) #[grayScale, flip, sharpFilter]

cam = cv2.VideoCapture(0)

img_counter = 0

def iD(time):
    return int(time.strftime("%m"))*10000000 + int(time.strftime("%d"))*100000 + int(time.strftime("%H")) * 1000 + int(time.strftime("%M")) * 10

def timeStamp(time, img):
    # ADD DATE 
    # raw and f string
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #org = (50, 50)
    #fontScale = 0.75
    #color = (255, 255, 255)
    #thickness = 2 #line thickness of 2 px
    return cv2.putText(img, f"{time}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                    0.75, (255, 255, 255), 2, cv2.LINE_AA)

def flip(img):
    return cv2.flip(img, 0)

def gScale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def sharpF(img):
    kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    return cv2.filter2D(img, -1, kernel)

print("Press \"i\" to input sequence or esc to exit.")
# main loop
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("Press \"i\" to input sequence, or esc to exit", frame)

    k = cv2.waitKey(1)

    key = k%256
    if key == 27: #"esc"
        print("escape--closing the app")
        break
    elif key == 105: #"i"
        print(f"last state: {lastState}")
        print("Key: clear - clear prev states | c - take pic | d - grayscale = ON | e - grayscale = OFF |\nf - flip 180 | g - sharp filter = ON | h - sharp filter = OFF")
        input = input("Sequence: ")
        comm = input.split(" ")
        while len(comm) > 0:
            next = comm.pop(0)
            if next == "c":
                time = datetime.datetime.now()
                img_name = f"opencv_frame_{iD(time) + img_counter}.png"
                print(img_name)
                cv2.imwrite(img_name, frame)
                path = rf"C:\Users\nicol\programs\Rocketry\opencvCamLibTesting\{img_name}" #ADD YOUR PATH HERE
                img = cv2.imread(path)
                if lastState[0]: #grayscale
                    img = gScale(img)
                if lastState[1]: #flipped 180 deg
                    img = flip(img)
                if lastState[2]: #sharpened filter 
                    img = sharpF(img)
                cv2.imwrite(img_name, timeStamp(time, img))
                print(f"screenshot taken, state: gScal - {lastState[0]} | flip - {lastState[1]} | sharp - {lastState[2]}")
                img_counter += 1  
            elif next == "d":
                lastState[0] = True 
            elif next == "e":
                lastState[0] = False
            elif next == "f":
                lastState[1] = True if not lastState[1] else False
            elif next == "g":
                lastState[2] = True
            elif next == "h":
                lastState[2] = False
            elif next == "clear":
                lastState = [False, False, False]
        del input
        
cam.release()
cv2.destroyAllWindows()
